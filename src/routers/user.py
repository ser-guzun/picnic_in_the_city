from fastapi import APIRouter, Depends

from src.dependencies.database import Session, get_db
from src.schemas.user import User, UserCreate
from src.services import user_service

router = APIRouter(dependencies=[Depends(get_db)])


@router.get("/users/", response_model=list[User], tags=["user"])
def read_users(db: Session = Depends(get_db)) -> list[User]:
    return user_service.get_users(db=db)


@router.get("/users/{user_id}", response_model=User, tags=["user"])
def read_user_by_id(user_id: int, db: Session = Depends(get_db)) -> User:
    return user_service.get_user_by_id(user_id=user_id, db=db)


@router.get(
    "/users&q=name:{user_name}", response_model=list[User], tags=["user"]
)
def read_users_by_name(
    user_name: str, db: Session = Depends(get_db)
) -> list[User]:
    return user_service.get_users_by_name(user_name=user_name, db=db)


@router.get("/users&q=age:{user_age}", response_model=list[User], tags=["user"])
def read_users_by_age(
    user_age: int, db: Session = Depends(get_db)
) -> list[User]:
    return user_service.get_users_by_age(user_age=user_age, db=db)


@router.get("/users&q=max_age/", response_model=list[User], tags=["user"])
def read_users_max_age(db: Session = Depends(get_db)) -> list[User]:
    return user_service.get_users_max_age(db=db)


@router.get("/users&q=min_age/", response_model=list[User], tags=["user"])
def read_users_min_age(db: Session = Depends(get_db)) -> list[User]:
    return user_service.get_users_min_age(db=db)


@router.post("/users/", response_model=User, tags=["user"])
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    return user_service.create_user(user=user, db=db)
