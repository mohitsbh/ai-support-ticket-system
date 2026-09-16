import pandas as pd
import numpy as np

def detect_anomalies(df):
    anomalies = []

    resolved = df[df['resolution_time_hrs'].notna() & (df['resolution_time_hrs'] > 0)]
    if len(resolved) > 0:
        mean_res = resolved['resolution_time_hrs'].mean()
        std_res = resolved['resolution_time_hrs'].std()
        if std_res > 0:
            long_resolution = resolved[resolved['resolution_time_hrs'] > mean_res + 2 * std_res]
            for _, row in long_resolution.iterrows():
                anomalies.append({
                    "ticket_id": row['ticket_id'],
                    "type": "long_resolution",
                    "severity": "high",
                    "detail": f"Resolution took {row['resolution_time_hrs']:.1f} hrs (avg: {mean_res:.1f} hrs)",
                    "category": row['category'],
                    "priority": row['priority']
                })

    high_priority_open = df[(df['priority'].isin(['High', 'Critical'])) & (df['status'] == 'Open')]
    for _, row in high_priority_open.iterrows():
        anomalies.append({
            "ticket_id": row['ticket_id'],
            "type": "unresolved_high_priority",
            "severity": "critical",
            "detail": f"{row['priority']} priority ticket is still Open",
            "category": row['category'],
            "priority": row['priority']
        })

    escalated_open = df[df['status'] == 'Escalated']
    for _, row in escalated_open.iterrows():
        anomalies.append({
            "ticket_id": row['ticket_id'],
            "type": "escalated_not_resolved",
            "severity": "high",
            "detail": f"Ticket is Escalated and not resolved",
            "category": row['category'],
            "priority": row['priority']
        })

    if len(resolved) > 0:
        high_response = resolved[resolved['response_time_hrs'] > resolved['response_time_hrs'].quantile(0.95)]
        for _, row in high_response.iterrows():
            anomalies.append({
                "ticket_id": row['ticket_id'],
                "type": "high_response_time",
                "severity": "medium",
                "detail": f"Response time: {row['response_time_hrs']:.1f} hrs (above 95th percentile)",
                "category": row['category'],
                "priority": row['priority']
            })

    return anomalies

def get_anomaly_summary(df):
    anomalies = detect_anomalies(df)
    summary = {}
    for a in anomalies:
        t = a['type']
        summary[t] = summary.get(t, 0) + 1
    return {"total_anomalies": len(anomalies), "by_type": summary}