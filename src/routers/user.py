from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies.database import get_session
from src.schemas.user import User, UserCreate
from src.services import user_service

router = APIRouter(dependencies=[Depends(get_session)])


@router.get("/users/", response_model=list[User], tags=["user"])
async def read_users(
    session: AsyncSession = Depends(get_session),
) -> list[User]:
    users = await user_service.get_users(session=session)
    return [user for user in users]


@router.get("/users/{user_id}", response_model=User, tags=["user"])
async def read_user_by_id(
    user_id: int, session: AsyncSession = Depends(get_session)
) -> User:
    user = await user_service.get_user_by_id(user_id=user_id, session=session)
    return user


@router.get(
    "/users&q=name:{user_name}", response_model=list[User], tags=["user"]
)
async def read_users_by_name(
    user_name: str, session: AsyncSession = Depends(get_session)
) -> list[User]:
    users = await user_service.get_users_by_name(
        user_name=user_name, session=session
    )
    return [user for user in users]


@router.get("/users&q=age:{user_age}", response_model=list[User], tags=["user"])
async def read_users_by_age(
    user_age: int, session: AsyncSession = Depends(get_session)
) -> list[User]:
    users = await user_service.get_users_by_age(
        user_age=user_age, session=session
    )
    return [user for user in users]


@router.get("/users&q=max_age/", response_model=list[User], tags=["user"])
async def read_users_max_age(
    session: AsyncSession = Depends(get_session),
) -> list[User]:
    users = await user_service.get_users_max_age(session=session)
    return [user for user in users]


@router.get("/users&q=min_age/", response_model=list[User], tags=["user"])
async def read_users_min_age(
    session: AsyncSession = Depends(get_session),
) -> list[User]:
    users = await user_service.get_users_min_age(session=session)
    return [user for user in users]


@router.post("/users/", response_model=User, tags=["user"])
async def create_user(
    user: UserCreate, session: AsyncSession = Depends(get_session)
) -> User:
    user = await user_service.create_user(user=user, session=session)
    return user
