from unittest.mock import AsyncMock

from fastapi.testclient import TestClient

from app.db.connection import DatabaseConnectionError
from app.main import app


def test_api_remains_available_when_mongodb_is_unavailable(monkeypatch) -> None:
    connect = AsyncMock(side_effect=DatabaseConnectionError("unavailable"))
    close = AsyncMock()
    monkeypatch.setattr("app.main.database.connect", connect)
    monkeypatch.setattr("app.main.database.close", close)

    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok"}
        assert client.get("/api/info").status_code == 200
        assert client.get("/docs").status_code == 200

    connect.assert_awaited_once()
    close.assert_awaited_once()


def test_database_health_reports_connected_without_sensitive_details(monkeypatch) -> None:
    ping = AsyncMock(return_value=True)
    monkeypatch.setattr("app.routes.health.database.ping", ping)

    response = TestClient(app).get("/health/database")

    assert response.status_code == 200
    assert response.json() == {"status": "connected"}
    ping.assert_awaited_once()


def test_database_health_reports_unavailable_without_sensitive_details(monkeypatch) -> None:
    ping = AsyncMock(return_value=False)
    monkeypatch.setattr("app.routes.health.database.ping", ping)

    response = TestClient(app).get("/health/database")

    assert response.status_code == 503
    assert response.json() == {"status": "unavailable"}
    ping.assert_awaited_once()
