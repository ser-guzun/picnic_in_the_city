from sqlalchemy.orm import Session

from src.models.models import Picnic, PicnicUser
from src.schemas.picnic import PicnicCreate
from src.services.user_service import get_user_by_id


def get_picnics(db: Session):
    return db.query(Picnic).all()


def get_picnic_by_id(picnic_id: int, db: Session):
    return db.query(Picnic).filter(Picnic.id == picnic_id).first()


def get_picnics_by_reason(picnic_reason: str, db: Session):
    return db.query(Picnic).filter(Picnic.reason == picnic_reason).all()


def create_picnic(picnic: PicnicCreate, db: Session) -> Picnic:
    db_picnic = Picnic(
        reason=picnic.reason,
        city_id=picnic.city_id,
        time=picnic.time,
    )
    db.add(db_picnic)
    db.commit()
    db.refresh(db_picnic)

    if picnic.users:
        users = [
            get_user_by_id(user_id=user.id, db=db) for user in picnic.users
        ]
        for user in users:
            registration_user_to_picnic(
                picnic_id=db_picnic.id, user_id=user.id, db=db
            )

    return db_picnic


def registration_user_to_picnic(picnic_id: int, user_id: int, db: Session):
    picnic_user = PicnicUser(picnic_id=picnic_id, user_id=user_id)
    db.add(picnic_user)
    db.commit()
    db.refresh(picnic_user)
    return picnic_user
