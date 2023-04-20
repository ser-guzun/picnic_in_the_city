from fastapi import APIRouter, Depends, HTTPException

from src.dependencies.database import async_session, get_session
from src.schemas.city import City, CityCreate
from src.services import city_service

router = APIRouter(dependencies=[Depends(get_session)])


@router.get("/cities/", response_model=list[City], tags=["city"])
def read_cities(db: async_session = Depends(get_session)) -> list[City]:
    return city_service.get_cities(db=db)


@router.get("/cities/{city_id}", response_model=City, tags=["city"])
def read_city_by_id(
    city_id: int, db: async_session = Depends(get_session)
) -> City:
    return city_service.get_city_by_id(city_id=city_id, db=db)


@router.get("/cities&q=name:{city_name}", response_model=City, tags=["city"])
def read_city_by_name(
    city_name: str, db: async_session = Depends(get_session)
) -> City:
    return city_service.get_city_by_name(city_name=city_name, db=db)


@router.post("/cities/", response_model=City, tags=["city"])
def create_city(
    city: CityCreate, db: async_session = Depends(get_session)
) -> City:
    db_city = city_service.get_city_by_name(city_name=city.name, db=db)
    if db_city:
        raise HTTPException(status_code=400, detail="City already created")
    return city_service.create_city(city=city, db=db)
