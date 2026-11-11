from fastapi import APIRouter, Response

from app.db.connection import database

router = APIRouter()


@router.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Report API process liveness; external dependencies are not checked."""
    return {"status": "ok"}


@router.get("/health/database", tags=["health"])
async def database_health_check(response: Response) -> dict[str, str]:
    """Report MongoDB connectivity without exposing connection details."""
    if await database.ping():
        return {"status": "connected"}

    response.status_code = 503
    return {"status": "unavailable"}