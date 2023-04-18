from typing import Any

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from src.models.models import User
from src.schemas.user import UserCreate


def get_users(db: Session) -> list[User]:
    return db.query(User).all()


def get_user_by_id(user_id: int, db: Session) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_users_by_name(user_name: str, db: Session) -> list[User]:
    return db.query(User).filter(User.name == user_name).all()


def get_users_by_age(user_age: int, db: Session) -> list[User]:
    return (
        db.query(User)
        .filter(User.age == user_age)
        .order_by(desc(User.age))
        .all()
    )


def get_users_max_age(db: Session) -> list[User]:
    max_age = db.query(func.max(User.age)).scalar_subquery()
    return (
        db.query(User)
        .filter(User.age == max_age)
        .order_by(desc(User.age))
        .all()
    )


def get_users_min_age(db: Session) -> list[User]:
    min_age = db.query(func.min(User.age)).scalar_subquery()
    return (
        db.query(User)
        .filter(User.age == min_age)
        .order_by(desc(User.age))
        .all()
    )


def create_user(user: UserCreate, db: Session) -> User:
    user = User(name=user.name, surname=user.surname, age=user.age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
