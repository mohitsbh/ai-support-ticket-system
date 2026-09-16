import pandas as pd
import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "support_tickets.csv")

def load_data():
    df = pd.read_csv(CSV_PATH)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['response_time_hrs'] = pd.to_numeric(df['response_time_hrs'], errors='coerce')
    df['resolution_time_hrs'] = pd.to_numeric(df['resolution_time_hrs'], errors='coerce')
    df['customer_rating'] = pd.to_numeric(df['customer_rating'], errors='coerce')
    return df

def get_stats(df):
    total = len(df)
    open_tickets = len(df[df['status'] == 'Open'])
    resolved = len(df[df['status'] == 'Resolved'])
    escalated = len(df[df['status'] == 'Escalated'])
    critical = len(df[df['priority'] == 'Critical'])
    critical_open = len(df[(df['priority'] == 'Critical') & (df['status'] == 'Open')])
    return {
        "total_tickets": total,
        "open_tickets": open_tickets,
        "resolved_tickets": resolved,
        "escalated_tickets": escalated,
        "critical_tickets": critical,
        "critical_open": critical_open
    }

def get_agent_stats(df):
    resolved_df = df[df['status'] == 'Resolved']
    agent_resolved = resolved_df['agent_id'].value_counts().to_dict()
    agent_ratings = resolved_df.groupby('agent_id')['customer_rating'].mean().round(2).to_dict()
    agent_resolution_time = resolved_df.groupby('agent_id')['resolution_time_hrs'].mean().round(2).to_dict()
    return {"resolved_by": agent_resolved, "avg_ratings": agent_ratings, "avg_resolution_hrs": agent_resolution_time}

def get_category_stats(df):
    return df.groupby('category').agg(
        count=('ticket_id', 'count'),
        avg_rating=('customer_rating', 'mean'),
        avg_resolution=('resolution_time_hrs', 'mean')
    ).round(2).to_dict('index')

def filter_by_date(df, days=30):
    cutoff = df['created_at'].max() - timedelta(days=days)
    return df[df['created_at'] >= cutoff]