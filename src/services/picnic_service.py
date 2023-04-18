from sqlalchemy.orm import Session

from src.models.models import Picnic
from src.schemas.picnic import PicnicCreate


def get_picnics(db: Session):
    return db.query(Picnic).all()


def get_picnic_by_id(picnic_id: int, db: Session):
    return db.query(Picnic).filter(Picnic.id == picnic_id).first()


def get_picnics_by_reason(picnic_reason: str, db: Session):
    return db.query(Picnic).filter(Picnic.reason == picnic_reason).all()


def create_picnic(picnic: PicnicCreate, db: Session):
    picnic = Picnic(reason=picnic.reason, city_id=picnic.city_id, time=picnic.time)
    db.add(picnic)
    db.commit()
    db.refresh(picnic)
    return picnic
