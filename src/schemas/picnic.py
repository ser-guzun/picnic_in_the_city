from datetime import datetime

from pydantic import BaseModel

from src.schemas.base import Base


class PicnicBase(BaseModel):
    reason: str
    city_id: int
    time: datetime


class Picnic(Base, PicnicBase):
    class Config:
        orm_mode = True


class PicnicCreate(PicnicBase):
    pass
