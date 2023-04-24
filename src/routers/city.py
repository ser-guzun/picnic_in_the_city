from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies.database import get_session
from src.schemas.city import City, CityCreate
from src.services import city_service

router = APIRouter(dependencies=[Depends(get_session)])


@router.get("/cities/", response_model=list[City], tags=["city"])
async def read_cities(
    session: AsyncSession = Depends(get_session),
) -> list[City]:
    cities = await city_service.get_cities(session=session)
    return [city for city in cities]


@router.get("/cities/{city_id}", response_model=City, tags=["city"])
async def read_city_by_id(
    city_id: int, session: AsyncSession = Depends(get_session)
) -> City:
    city = await city_service.get_city_by_id(city_id=city_id, session=session)
    return city


@router.get("/cities&q=name:{city_name}", response_model=City, tags=["city"])
async def read_city_by_name(
    city_name: str, session: AsyncSession = Depends(get_session)
) -> City:
    city = await city_service.get_city_by_name(
        city_name=city_name, session=session
    )
    return city


@router.post("/cities/", response_model=City, tags=["city"])
async def create_city(
    city: CityCreate, session: AsyncSession = Depends(get_session)
) -> City:
    db_city = await city_service.get_city_by_name(
        city_name=city.name, session=session
    )
    if db_city:
        raise HTTPException(status_code=400, detail="City already created")
    return await city_service.create_city(city=city, session=session)
