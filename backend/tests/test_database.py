import asyncio
from unittest.mock import AsyncMock, MagicMock, Mock

import pytest
from pydantic import ValidationError
from pymongo.errors import ConfigurationError, ServerSelectionTimeoutError

from app.core.config import Settings
from app.db.connection import DatabaseConnectionError, MongoDatabase
from app.schemas import EmergencyContactSchema, UserSchema


def test_mongodb_settings_load_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MONGODB_URI", "mongodb://db.example:27017")
    monkeypatch.setenv("MONGODB_DATABASE", "abhaya_test")
    monkeypatch.setenv("MONGODB_SERVER_SELECTION_TIMEOUT_MS", "250")

    settings = Settings(_env_file=None)

    assert settings.mongodb_uri == "mongodb://db.example:27017"
    assert settings.mongodb_database == "abhaya_test"
    assert settings.mongodb_server_selection_timeout_ms == 250


def test_mongodb_connection_pings_and_closes(monkeypatch: pytest.MonkeyPatch) -> None:
    client = MagicMock()
    client.admin.command = AsyncMock()
    client.close = AsyncMock()
    constructor = Mock(return_value=client)
    monkeypatch.setattr("app.db.connection.AsyncMongoClient", constructor)
    database = MongoDatabase()
    settings = Settings(_env_file=None)

    async def exercise_connection() -> None:
        await database.connect(settings)
        assert database.client is client
        assert database.database is client[settings.mongodb_database]
        client.admin.command.assert_awaited_once_with("ping")
        constructor.assert_called_once_with(
            settings.mongodb_uri,
            serverSelectionTimeoutMS=settings.mongodb_server_selection_timeout_ms,
        )

        await database.close()
        client.close.assert_awaited_once()
        assert database.client is None
        assert database.database is None

    asyncio.run(exercise_connection())


def test_mongodb_connection_failure_is_sanitized_and_releases_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = Mock()
    client.admin.command = AsyncMock(
        side_effect=ServerSelectionTimeoutError("failure included private connection details")
    )
    client.close = AsyncMock()
    monkeypatch.setattr("app.db.connection.AsyncMongoClient", Mock(return_value=client))
    database = MongoDatabase()

    async def attempt_connection() -> None:
        with pytest.raises(DatabaseConnectionError) as error:
            await database.connect(Settings(_env_file=None))

        assert "private" not in str(error.value)
        client.close.assert_awaited_once()
        assert database.client is None
        assert database.database is None

    asyncio.run(attempt_connection())


def test_invalid_mongodb_uri_is_reported_as_connection_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.db.connection.AsyncMongoClient",
        Mock(side_effect=ConfigurationError("private URI details")),
    )
    database = MongoDatabase()

    async def attempt_connection() -> None:
        with pytest.raises(DatabaseConnectionError) as error:
            await database.connect(Settings(_env_file=None))

        assert "private" not in str(error.value)
        assert database.client is None
        assert database.database is None

    asyncio.run(attempt_connection())


def test_user_schema_does_not_accept_passwords() -> None:
    with pytest.raises(ValidationError):
        UserSchema(full_name="Example User", email="example@example.com", password="secret")

    contact = EmergencyContactSchema(
        user_id="user-1",
        name="Trusted Contact",
        phone_number="+10000000000",
    )
    assert contact.phone_number == "+10000000000"
