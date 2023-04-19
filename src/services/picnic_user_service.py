from sqlalchemy.orm import Session

from src.models.models import PicnicUser


def registration_user_to_picnic(
    picnic_id: int, user_id: int, db: Session
) -> PicnicUser:
    picnic_user = PicnicUser(picnic_id=picnic_id, user_id=user_id)
    db.add(picnic_user)
    db.commit()
    db.refresh(picnic_user)
    return picnic_user


def get_users_by_picnic_id(picnic_id: int, db: Session) -> list[PicnicUser]:
    return db.query(PicnicUser).filter(PicnicUser.picnic_id == picnic_id).all()
