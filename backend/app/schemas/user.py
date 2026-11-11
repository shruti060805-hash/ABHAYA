from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class UserSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str | None = None
    full_name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=254)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
