# ABHAYA Backend

This directory contains the FastAPI service foundation and asynchronous MongoDB connection lifecycle. It provides `GET /health` for process liveness and `GET /api/info` for API metadata, along with user and emergency-contact data schemas. User/contact endpoints, authentication, SOS, notifications, location, and AI features are not implemented.

## Requirements

- Python 3.10 or newer

## Local setup

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment:

```bash
# Linux or macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies and create local configuration:

```bash
python -m pip install -r requirements.txt
cp .env.example .env
```

Run the API from this directory so the local `.env` file is loaded:

```bash
uvicorn app.main:app --reload
```

The OpenAPI UI is available at `http://127.0.0.1:8000/docs`. Check `http://127.0.0.1:8000/health` for API liveness, `http://127.0.0.1:8000/health/database` for MongoDB connectivity, and `http://127.0.0.1:8000/api/info` for API metadata. The database health route returns `{"status":"connected"}` after a successful ping or HTTP 503 with `{"status":"unavailable"}` when MongoDB cannot be reached; it never includes connection details.

## Configuration

`CORS_ORIGINS` is a comma-separated allow-list of exact origins. The example allows the Flutter web development origin on port 8080 for localhost and 127.0.0.1. Set only the origins needed by your local client; do not use `*`. Browser credentials are disabled.

MongoDB configuration:

- `MONGODB_URI`: MongoDB connection URI. For Atlas, set this to the cluster URI from the Atlas **Connect** dialog in your local `.env`; keep the URI private. The example points to a local MongoDB server and contains no credentials.
- `MONGODB_DATABASE`: database name (defaults to `abhaya`).
- `MONGODB_SERVER_SELECTION_TIMEOUT_MS`: maximum time to wait for a server during the startup ping (defaults to `1000`).

On startup the API pings MongoDB and logs a credential-free warning if the server is unavailable. The API remains available for liveness and metadata requests; database-backed features cannot work until MongoDB is configured and reachable. Keep real credentials in the ignored local `.env`, never in source control. The current backend does not send emergency notifications or make emergency calls.

User and emergency-contact schemas intentionally contain no password field. Authentication and persistence endpoints are not implemented; when added, passwords must be handled separately using secure password hashing.

## Tests

```bash
python -m pytest
```