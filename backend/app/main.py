import logging
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.errors import register_exception_handlers
from app.db.connection import DatabaseConnectionError, database
from app.routes.health import router as health_router
from app.routes.info import router as info_router

settings = get_settings()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    try:
        await database.connect(settings)
    except DatabaseConnectionError:
        logger.warning("MongoDB is unavailable; database-backed features are disabled.")
    try:
        yield
    finally:
        await database.close()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="ABHAYA backend foundation. Safety features are not implemented yet.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["Accept", "Authorization", "Content-Type"],
)

app.include_router(health_router)
app.include_router(info_router)
register_exception_handlers(app)