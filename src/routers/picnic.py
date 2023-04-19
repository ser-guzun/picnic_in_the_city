from fastapi import APIRouter, Depends

from src.dependencies.database import Session, get_db
from src.schemas.picnic import Picnic, PicnicCreate
from src.schemas.user import User
from src.services import picnic_service, picnic_user_service, user_service

router = APIRouter(dependencies=[Depends(get_db)])


@router.get("/picnics/", response_model=list[Picnic], tags=["picnic"])
def read_picnics(db: Session = Depends(get_db)) -> list[Picnic]:
    picnics = picnic_service.get_picnics(db=db)
    for picnic in picnics:
        picnic_users = picnic_user_service.get_users_by_picnic_id(
            picnic_id=picnic.id, db=db
        )
        if picnic_users:
            users = [
                user_service.get_user_by_id(user_id=picnic_user.user_id, db=db)
                for picnic_user in picnic_users
            ]
            picnic.users = users
    return picnics


@router.get("/picnics/{picnic_id}", response_model=Picnic, tags=["picnic"])
def read_picnic_by_id(picnic_id: int, db: Session = Depends(get_db)) -> Picnic:
    return picnic_service.get_picnic_by_id(picnic_id=picnic_id, db=db)


@router.get(
    "/picnics&q=reason:{picnic_reason}",
    response_model=list[Picnic],
    tags=["picnic"],
)
def read_picnic_by_reason(
    picnic_reason: str, db: Session = Depends(get_db)
) -> list[Picnic]:
    return picnic_service.get_picnics_by_reason(
        picnic_reason=picnic_reason, db=db
    )


@router.post("/picnics/", response_model=Picnic, tags=["picnic"])
def create_picnic(
    picnic: PicnicCreate, db: Session = Depends(get_db)
) -> Picnic:
    db_picnic: Picnic = picnic_service.create_picnic(picnic=picnic, db=db)

    if picnic.users:
        users = [
            user_service.get_user_by_id(user_id=user.id, db=db)
            for user in picnic.users
        ]
        for user in users:
            picnic_user_service.registration_user_to_picnic(
                picnic_id=db_picnic.id, user_id=user.id, db=db
            )
        db_picnic.users = users

    return db_picnic


@router.put("/picnic_user/", response_model=list[User], tags=["picnic"])
def registration_users_to_picnic(
    picnic_id: int, user_ids: list[int], db: Session = Depends(get_db)
) -> list[User]:
    users = [
        user_service.get_user_by_id(user_id=user_id, db=db)
        for user_id in user_ids
    ]
    for user in users:
        picnic_user_service.registration_user_to_picnic(
            picnic_id=picnic_id, user_id=user.id, db=db
        )
    return users
