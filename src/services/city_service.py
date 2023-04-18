from sqlalchemy.orm import Session

from src.models.models import City
from src.schemas.city import CityCreate


def get_cities(db: Session):
    return db.query(City).all()


def get_city_by_id(city_id: int, db: Session):
    return db.query(City).filter(City.id == city_id).first()


def get_city_by_name(city_name: str, db: Session):
    return db.query(City).filter(City.name == city_name).first()


def create_city(city: CityCreate, db: Session):
    city = City(name=city.name)
    db.add(city)
    db.commit()
    db.refresh(city)
    return city
