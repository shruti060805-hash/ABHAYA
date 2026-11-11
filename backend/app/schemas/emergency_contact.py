from pydantic import BaseModel, ConfigDict, Field


class EmergencyContactSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str | None = None
    user_id: str
    name: str = Field(min_length=1, max_length=100)
    phone_number: str = Field(min_length=1, max_length=32)
    relationship: str | None = Field(default=None, max_length=50)
