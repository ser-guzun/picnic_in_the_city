from datetime import datetime

from pydantic import BaseModel, validator


class Base(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    @validator("created_at", "updated_at", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()
