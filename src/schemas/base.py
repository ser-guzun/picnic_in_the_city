from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class Base(BaseModel):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator("created_at", "updated_at", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()
