from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from src.database import Base


class City(Base):
    """Город"""
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=True)


class User(Base):
    """Пользователь"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=True)

    def __repr__(self):
        return f'<Пользователь {self.surname} {self.name}>'


class Picnic(Base):
    """Пикник"""
    __tablename__ = 'picnic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    time = Column(DateTime, nullable=False)

    def __repr__(self):
        return f'<Пикник {self.id}>'
