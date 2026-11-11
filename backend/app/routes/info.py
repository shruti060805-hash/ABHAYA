from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()


@router.get("/", tags=["information"])
@router.get("/api/info", tags=["information"])
async def api_info() -> dict[str, str]:
    settings = get_settings()
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "description": "ABHAYA backend foundation; application features are not implemented.",
    }