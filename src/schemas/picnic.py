from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.schemas.base import Base
from src.schemas.user import User


class PicnicBase(BaseModel):
    reason: str
    city_id: int
    time: datetime
    users: Optional[list[User]]


class Picnic(Base, PicnicBase):
    class Config:
        orm_mode = True


class PicnicCreate(PicnicBase):
    pass
