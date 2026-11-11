from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.errors import PyMongoError

from app.core.config import Settings, get_settings


class DatabaseConnectionError(RuntimeError):
    """Raised when the MongoDB server cannot be reached."""


class MongoDatabase:
    def __init__(self) -> None:
        self.client: AsyncMongoClient | None = None
        self.database: AsyncDatabase | None = None

    async def connect(self, settings: Settings | None = None) -> None:
        if self.client is not None and self.database is not None:
            return

        config = settings or get_settings()
        try:
            client = AsyncMongoClient(
                config.mongodb_uri,
                serverSelectionTimeoutMS=config.mongodb_server_selection_timeout_ms,
            )
        except PyMongoError as exc:
            raise DatabaseConnectionError("Unable to connect to MongoDB.") from exc

        try:
            await client.admin.command("ping")
        except PyMongoError as exc:
            await client.close()
            raise DatabaseConnectionError("Unable to connect to MongoDB.") from exc

        self.client = client
        self.database = client[config.mongodb_database]

    async def close(self) -> None:
        client, self.client = self.client, None
        self.database = None
        if client is not None:
            await client.close()

    async def ping(self) -> bool:
        if self.client is None or self.database is None:
            return False

        try:
            await self.client.admin.command("ping")
        except PyMongoError:
            return False
        return True


database = MongoDatabase()
