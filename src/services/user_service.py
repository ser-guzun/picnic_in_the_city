from sqlalchemy.orm import Session
from src.models.models import User
from src.schemas.user import UserCreate


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_name(user_name: str, db: Session):
    return db.query(User).filter(User.name == user_name).first()


def create_city(user: UserCreate, db: Session):
    user = User(name=user.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
