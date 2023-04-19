from pydantic import BaseModel

from src.schemas.base import Base


class PicnicUserBase(BaseModel):
    picnic_id: int
    user_id: int


class PicnicUser(Base, PicnicUserBase):
    class Config:
        orm_mode = True
