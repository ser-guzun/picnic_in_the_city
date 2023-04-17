from typing import Optional
from pydantic import BaseModel

from src.schemas.base import Base


class UserBase(BaseModel):
    name: str
    surname: str
    age: Optional[int]


class User(Base, UserBase):

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass

