from typing import Optional
from pydantic import BaseModel

from src.schemas.base import Base


class CityBase(BaseModel):
    name: Optional[str]


class City(Base, CityBase):

    class Config:
        orm_mode = True


class CityCreate(CityBase):
    pass

