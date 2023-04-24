from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import User
from src.schemas.user import UserCreate


async def get_users(session: AsyncSession) -> list[User]:
    users = await session.execute(select(User))
    return users.scalars().all()


async def get_user_by_id(user_id: int, session: AsyncSession) -> User:
    user = await session.execute(select(User).where(User.id == user_id))
    return user.scalar()


async def get_users_by_name(
    user_name: str, session: AsyncSession
) -> list[User]:
    users = await session.execute(select(User).where(User.name == user_name))
    return users.scalars().all()


async def get_users_by_age(user_age: int, session: AsyncSession) -> list[User]:
    users = await session.execute(
        select(User).where(User.age == user_age).order_by(desc(User.age))
    )
    return users.scalars().all()


async def get_users_max_age(session: AsyncSession) -> list[User]:
    max_age = await session.execute(func.max(User.age))
    users = await session.execute(
        select(User)
        .where(User.age == max_age.scalar())
        .order_by(desc(User.age))
    )
    return users.scalars().all()


async def get_users_min_age(session: AsyncSession) -> list[User]:
    min_age = await session.execute(func.min(User.age))
    users = await session.execute(
        select(User)
        .where(User.age == min_age.scalar())
        .order_by(desc(User.age))
    )
    return users.scalars().all()


async def create_user(user: UserCreate, session: AsyncSession) -> User:
    user = User(name=user.name, surname=user.surname, age=user.age)
    session.add(user)
    await session.commit()
    return user
