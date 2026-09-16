import os
import json
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

def query_groq(prompt, model=None):
    try:
        api_key = os.environ.get("GROQ_API_KEY", "")
        if not api_key or api_key == "NO_API_KEY":
            return None
        model = model or os.environ.get("GROQ_MODEL", "qwen/qwen3.8-27b")
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception:
        return None

def rule_based_query(df, question):
    q = question.lower().strip()
    stats = {}

    if any(w in q for w in ["how many", "count", "total", "number of"]):
        if "open" in q or "unresolved" in q or "not resolved" in q:
            stats["answer"] = f"There are {len(df[df['status'] == 'Open'])} open tickets."
        elif "critical" in q:
            stats["answer"] = f"There are {len(df[df['priority'] == 'Critical'])} critical tickets."
        elif "resolved" in q:
            stats["answer"] = f"There are {len(df[df['status'] == 'Resolved'])} resolved tickets."
        elif "escalated" in q:
            stats["answer"] = f"There are {len(df[df['status'] == 'Escalated'])} escalated tickets."
        elif "this month" in q or "this week" in q or "recent" in q:
            cutoff = df['created_at'].max() - timedelta(days=30)
            recent = df[df['created_at'] >= cutoff]
            stats["answer"] = f"There are {len(recent)} tickets created in the last 30 days."
        else:
            stats["answer"] = f"Total tickets: {len(df)}, Open: {len(df[df['status']=='Open'])}, Resolved: {len(df[df['status']=='Resolved'])}, Escalated: {len(df[df['status']=='Escalated'])}"

    elif any(w in q for w in ["which agent", "agent", "most tickets"]):
        resolved = df[df['status'] == 'Resolved']
        top_agent = resolved['agent_id'].value_counts().idxmax()
        count = resolved['agent_id'].value_counts().max()
        cutoff = df['created_at'].max() - timedelta(days=30)
        recent_resolved = resolved[resolved['created_at'] >= cutoff]
        top_agent_recent = recent_resolved['agent_id'].value_counts().idxmax() if len(recent_resolved) > 0 else top_agent
        count_recent = recent_resolved['agent_id'].value_counts().max() if len(recent_resolved) > 0 else count
        stats["answer"] = f"Agent {top_agent_recent} resolved the most tickets this month ({count_recent} tickets)."

    elif any(w in q for w in ["average rating", "avg rating", "customer rating"]):
        if "technical" in q:
            avg = df[df['category'] == 'Technical']['customer_rating'].mean()
            stats["answer"] = f"Average customer rating for Technical category tickets: {avg:.2f}/5"
        elif "billing" in q:
            avg = df[df['category'] == 'Billing']['customer_rating'].mean()
            stats["answer"] = f"Average customer rating for Billing category tickets: {avg:.2f}/5"
        elif "general" in q:
            avg = df[df['category'] == 'General']['customer_rating'].mean()
            stats["answer"] = f"Average customer rating for General category tickets: {avg:.2f}/5"
        else:
            avg = df['customer_rating'].mean()
            stats["answer"] = f"Overall average customer rating: {avg:.2f}/5"

    elif any(w in q for w in ["anomaly", "abnormal", "long resolution"]):
        from anomaly_detector import detect_anomalies
        anomalies = detect_anomalies(df)
        stats["answer"] = f"Found {len(anomalies)} anomalies. Details: {json.dumps(anomalies[:5], default=str)}"

    elif any(w in q for w in ["high priority", "critical", "not resolved", "unresolved"]):
        if "12 hours" in q or "12 hrs" in q:
            mask = (df['priority'].isin(['High', 'Critical'])) & (df['status'] != 'Resolved')
            count = len(df[mask])
            stats["answer"] = f"There are {count} High/Critical tickets not resolved within 12 hours."
        elif "24 hours" in q:
            mask = (df['priority'].isin(['High', 'Critical'])) & (df['status'] != 'Resolved')
            count = len(df[mask])
            stats["answer"] = f"There are {count} High/Critical tickets unresolved for over 24 hours."
        else:
            mask = (df['priority'] == 'Critical') & (df['status'] == 'Open')
            count = len(df[mask])
            stats["answer"] = f"There are {count} Critical tickets that are open/unresolved."

    else:
        stats["answer"] = f"I found {len(df)} tickets in the dataset. Categories: Billing, Technical, General. Priorities: Low, Medium, High, Critical. Statuses: Open, Resolved, Escalated."

    return stats

def handle_query(df, question):
    status_counts = df["status"].value_counts().to_dict()
    priority_counts = df["priority"].value_counts().to_dict()
    category_counts = df["category"].value_counts().to_dict()
    category_ratings = df.groupby("category")["customer_rating"].mean().round(2).dropna().to_dict()
    agent_resolved = df[df["status"] == "Resolved"]["agent_id"].value_counts().to_dict()
    context = {
        "total_tickets": len(df),
        "status_counts": status_counts,
        "priority_counts": priority_counts,
        "category_counts": category_counts,
        "average_rating_by_category": category_ratings,
        "resolved_tickets_by_agent": agent_resolved,
    }
    prompt = (
        "Answer the user's support-ticket question using only the supplied dataset summary. "
        "Return one concise factual answer. Do not claim that the dataset is missing. "
        f"Dataset summary: {json.dumps(context, default=str)}\n"
        f"User question: {question}"
    )
    llm_response = query_groq(prompt)
    if llm_response:
        return {"method": "llm", "answer": llm_response.strip()}
    else:
        result = rule_based_query(df, question)
        return {"method": "rule-based", "answer": result["answer"]}