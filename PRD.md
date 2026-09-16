# Product Requirements Document
## AI Support Ticket Analysis System

**Status:** MVP implemented
**Version:** 1.0
**Owner:** Support Operations / Engineering
**Last Updated:** 2026-09-16

## 1. Product Summary

The AI Support Ticket Analysis System helps support teams understand ticket volume, identify operational risks, and answer business questions using natural language. It combines a Pandas-based ticket data layer, FastAPI REST endpoints, a browser UI, Groq LLM responses, and a rule-based fallback when the LLM is unavailable.

## 2. Problem Statement

Support teams need quick answers about ticket status, priority, resolution performance, customer ratings, and anomalies. Manual CSV analysis is slow and makes it difficult to identify unresolved high-priority work or agent performance trends.

## 3. Goals

- Provide a single interface for support ticket analysis.
- Allow users to ask factual questions in plain English.
- Surface resolution-time and priority-related anomalies.
- Show ticket, category, and agent performance statistics.
- Remain usable without an active LLM API connection through deterministic fallback logic.
- Expose the core capabilities through documented REST endpoints.

## 4. Non-Goals

- Creating, editing, or assigning support tickets.
- Replacing a production ticketing or CRM system.
- Making autonomous customer or agent decisions.
- Guaranteeing answers to arbitrary questions outside the available dataset.
- Real-time ingestion from external ticketing platforms in the MVP.

## 5. Target Users

### Primary Users

- Support managers reviewing team performance.
- Support operations analysts investigating ticket trends.
- AI or engineering evaluators testing data-analysis workflows.

### User Needs

- Quickly know how many tickets are open, resolved, escalated, or critical.
- Identify unresolved high-priority tickets.
- Compare agent resolution counts, ratings, and resolution times.
- Investigate unusual response or resolution behavior.
- Ask questions without writing Pandas queries or SQL.

## 6. MVP Scope

### 6.1 Data Ingestion

- Load support ticket records from `support_tickets.csv`.
- Parse ticket creation dates and numeric analysis fields.
- Support the current dataset of 500 tickets.
- Calculate statistics from the loaded dataset at application startup.

### 6.2 Natural-Language Querying

- Accept a user question through the UI or `/api/query`.
- Attempt a concise factual answer using Groq.
- Load the Groq credential from `GROQ_API_KEY` in `.env`.
- Fall back to deterministic rule-based answers when the key is missing, invalid, or the LLM request fails.
- Return the selected response method: `llm` or `rule-based`.

Supported MVP query categories include:

- Open, resolved, escalated, critical, and total ticket counts.
- Top agent by recent resolved ticket count.
- Average ratings by category or overall.
- High-priority unresolved tickets.
- Detected anomalies.

### 6.3 Anomaly Detection

The system must identify and summarize:

- Long resolution times above the configured statistical threshold.
- Unresolved high-priority tickets.
- Escalated tickets that remain unresolved.
- High response times above the configured percentile threshold.

Users can filter anomaly analysis by a number of recent days.

### 6.4 Dashboard and UI

The browser UI must provide:

- Total, open, critical, resolved, and escalated ticket metrics.
- A natural-language question input.
- Preset questions for common workflows.
- The answer and response method.
- Anomaly detection with a configurable day filter.
- Agent resolution statistics, ratings, and average resolution times.

### 6.5 REST API

| Endpoint | Method | Requirement |
|---|---|---|
| `/` | GET | Return the browser dashboard. |
| `/api/health` | GET | Return service status, dataset count, and model mode. |
| `/api/query` | POST | Accept `{ "question": "..." }` and return an answer. Reject blank questions. |
| `/api/anomalies?days=30` | GET | Return anomaly records, summary, filter, and analyzed ticket count. |
| `/api/stats` | GET | Return overall, agent, category, and date-range statistics. |
| `/api/agents` | GET | Return agent resolution and performance statistics. |

## 7. Functional Requirements

- **FR-01:** The application loads the CSV using a path relative to the project directory.
- **FR-02:** The service starts with `python run.py`.
- **FR-03:** The service is reachable at `http://127.0.0.1:8080` in a local browser.
- **FR-04:** Missing or unusable Groq credentials must not prevent the application from starting.
- **FR-05:** Blank natural-language questions return HTTP 400.
- **FR-06:** Unexpected query, statistics, or anomaly failures return HTTP 500 with an error detail.
- **FR-07:** Anomaly results include ticket identifier, anomaly type, severity, and explanatory detail where available.
- **FR-08:** API responses use JSON except for the dashboard HTML response.
- **FR-09:** Secrets must be read from environment configuration and excluded from version control.

## 8. Non-Functional Requirements

- **Availability:** Local startup must work without a Groq key through rule-based fallback.
- **Performance:** Standard dataset queries should return within 2 seconds without an LLM call.
- **Usability:** A first-time user should be able to open the dashboard and run a preset query without documentation.
- **Security:** API keys must never be hardcoded, logged, or committed. `.env` remains local and `.env.example` contains only a placeholder.
- **Maintainability:** Data loading, anomaly detection, LLM handling, API routing, and UI remain separated into focused modules.
- **Compatibility:** The application runs with the pinned Python dependencies in `requirements.txt`.

## 9. Success Metrics

- At least 95% of valid MVP query requests return a response.
- 100% of startup and health checks succeed without a Groq key.
- Users can retrieve dashboard statistics and anomaly results through the UI.
- Rule-based fallback provides an answer for all documented query examples.
- No secret values appear in source control or application output.

## 10. Acceptance Criteria

1. Running `pip install -r requirements.txt` installs all required dependencies.
2. Running `python run.py` starts the service on port 8080.
3. `GET /api/health` returns HTTP 200 and reports the loaded ticket count.
4. `POST /api/query` returns HTTP 200 for a valid question.
5. `POST /api/query` returns HTTP 400 for an empty question.
6. The same valid query remains usable when Groq is unavailable through rule-based fallback.
7. `GET /api/anomalies?days=30` returns a summary and anomaly list.
8. `GET /api/stats` returns overall, category, agent, and date-range data.
9. The dashboard loads at `http://127.0.0.1:8080/` and can run a preset question.
10. A real Groq key can be supplied through `.env` without changing Python source code.

## 11. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Groq API is unavailable or rate-limited | Use the rule-based fallback and expose the response method. |
| LLM response is not grounded in the dataset | Keep prompts factual and concise; prioritize deterministic rules for supported patterns. |
| CSV schema changes | Validate required columns during data loading in a future hardening phase. |
| Dataset is static | Add scheduled or event-based ingestion in a future release. |
| Sensitive data enters prompts | Add field filtering, masking, and an explicit data-retention policy before production use. |
| Local port is already occupied | Stop the existing process or configure a different port before startup. |

## 12. Future Roadmap

### Phase 2

- Add schema validation and clearer startup errors.
- Add automated unit and API tests.
- Add pagination and sorting for anomaly and agent results.
- Add configurable host and port environment variables.
- Add structured application logging and request timing.

### Phase 3

- Connect to a live ticketing platform.
- Add authentication and role-based access.
- Add historical trend charts and exportable reports.
- Add query evaluation and feedback collection.
- Add monitoring, rate limiting, and production deployment configuration.

## 13. Technical Dependencies

- Python 3.x
- FastAPI and Uvicorn
- Pandas and NumPy
- Groq Python SDK
- python-dotenv
- Vanilla HTML, CSS, and JavaScript

## 14. Configuration

Create a local `.env` file from `.env.example` and set:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The key is optional for MVP operation because the rule-based fallback remains available.
