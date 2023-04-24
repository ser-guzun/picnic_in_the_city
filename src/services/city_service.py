from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import City
from src.schemas.city import CityCreate


async def get_cities(session: AsyncSession) -> list[City]:
    cities = await session.execute(select(City))
    return cities.scalars().all()


async def get_city_by_id(city_id: int, session: AsyncSession) -> City:
    city = await session.execute(select(City).where(City.id == city_id))
    return city.scalar()


async def get_city_by_name(city_name: str, session: AsyncSession) -> City:
    city = await session.execute(select(City).where(City.name == city_name))
    return city.scalar()


async def create_city(city: CityCreate, session: AsyncSession):
    city = City(name=city.name)
    session.add(city)
    await session.commit()
    return city
