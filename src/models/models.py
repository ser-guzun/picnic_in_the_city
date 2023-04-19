from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from src.dependencies import Base


class Picnic(Base):
    """Пикник"""

    __tablename__ = "picnic"

    id = Column(Integer, primary_key=True, autoincrement=True)
    reason = Column(String, nullable=False, default="Without reason")
    city_id = Column(
        Integer, ForeignKey("city.id", ondelete="CASCADE"), nullable=False
    )
    city = relationship("City", back_populates="picnics")
    time = Column(DateTime, nullable=False)
    user = relationship(
        "User", secondary="picnic_user", back_populates="picnic"
    )
    created_at = Column(DateTime(), nullable=False, default=func.now())
    updated_at = Column(DateTime(), nullable=False, default=func.now())

    def __repr__(self):
        return f"<Пикник {self.id}>"


class PicnicUser(Base):
    """Гости, приглашенные на пикник"""

    __tablename__ = "picnic_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    picnic_id = Column(Integer, ForeignKey("picnic.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    created_at = Column(DateTime(), nullable=False, default=func.now())
    updated_at = Column(DateTime(), nullable=False, default=func.now())


class City(Base):
    """Город"""

    __tablename__ = "city"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(), nullable=False, default=func.now())
    updated_at = Column(DateTime(), nullable=False, default=func.now())
    picnics = relationship(
        Picnic,
        back_populates="city",
        cascade="save-update, merge, delete",
        passive_deletes=True,
    )


class User(Base):
    """Пользователь"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    picnic = relationship(
        Picnic, secondary="picnic_user", back_populates="user"
    )
    created_at = Column(DateTime(), nullable=False, default=func.now())
    updated_at = Column(DateTime(), nullable=False, default=func.now())

    def __repr__(self):
        return f"<Пользователь {self.surname} {self.name}>"
