from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

from data_loader import load_data, get_stats, get_agent_stats, get_category_stats, filter_by_date
from anomaly_detector import detect_anomalies, get_anomaly_summary
from llm_handler import handle_query

app = FastAPI(title="AI Support Ticket Analysis System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

df = load_data()

_html_path = os.path.join(PROJECT_DIR, "templates", "index.html")
with open(_html_path, "r", encoding="utf-8") as _f:
    HTML_PAGE = _f.read()

@app.get("/")
async def root():
    return HTMLResponse(content=HTML_PAGE)

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "AI Support Ticket Analysis System is running",
        "total_tickets": len(df),
        "model": "Groq qwen/qwen3.8-27b (fallback: rule-based)"
    }

@app.post("/api/query")
async def nl_query(req: QueryRequest):
    if not req.question or not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    try:
        result = handle_query(df, req.question)
        result["question"] = req.question
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/anomalies")
async def get_anomalies(days: Optional[int] = 30):
    try:
        filtered = filter_by_date(df, days)
        anomalies = detect_anomalies(filtered)
        summary = get_anomaly_summary(filtered)
        return JSONResponse(content={
            "anomalies": anomalies,
            "summary": summary,
            "days_filter": days,
            "total_tickets_analyzed": len(filtered)
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/stats")
async def get_statistics():
    try:
        stats = get_stats(df)
        agent_stats = get_agent_stats(df)
        category_stats = get_category_stats(df)
        return JSONResponse(content={
            "statistics": stats,
            "agent_stats": agent_stats,
            "category_stats": category_stats,
            "date_range": {
                "start": str(df['created_at'].min()),
                "end": str(df['created_at'].max())
            }
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agents")
async def get_agents():
    try:
        agent_stats = get_agent_stats(df)
        return JSONResponse(content=agent_stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)