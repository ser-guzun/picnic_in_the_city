from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies.database import get_session
from src.schemas.picnic import Picnic, PicnicCreate
from src.services import picnic_service, picnic_user_service, user_service

router = APIRouter(dependencies=[Depends(get_session)])


@router.get("/picnics/", response_model=list[Picnic], tags=["picnic"])
async def read_picnics(
    session: AsyncSession = Depends(get_session),
) -> list[Picnic]:
    picnics = await picnic_service.get_picnics(session=session)
    for picnic in picnics:
        picnic_users = await picnic_user_service.get_users_by_picnic_id(
            picnic_id=picnic.id, session=session
        )
        if picnic_users:
            users = [
                await user_service.get_user_by_id(
                    user_id=picnic_user.user_id, session=session
                )
                for picnic_user in picnic_users
            ]
            picnic.users = users
    return picnics


@router.get("/picnics/{picnic_id}", response_model=Picnic, tags=["picnic"])
async def read_picnic_by_id(
    picnic_id: int, session: AsyncSession = Depends(get_session)
) -> Picnic:
    picnic = await picnic_service.get_picnic_by_id(
        picnic_id=picnic_id, session=session
    )
    return picnic


@router.get(
    "/picnics&q=reason:{picnic_reason}",
    response_model=list[Picnic],
    tags=["picnic"],
)
async def read_picnic_by_reason(
    picnic_reason: str, session: AsyncSession = Depends(get_session)
) -> list[Picnic]:
    picnic = await picnic_service.get_picnics_by_reason(
        picnic_reason=picnic_reason, session=session
    )
    return picnic


@router.post("/picnics/", response_model=Picnic, tags=["picnic"])
async def create_picnic(
    picnic: PicnicCreate, session: AsyncSession = Depends(get_session)
) -> Picnic:
    db_picnic: Picnic = await picnic_service.create_picnic(
        picnic=picnic, session=session
    )

    if picnic.users:
        users = [
            await user_service.get_user_by_id(user_id=user.id, session=session)
            for user in picnic.users
        ]
        for user in users:
            await picnic_user_service.registration_user_to_picnic(
                picnic_id=db_picnic.id, user_id=user.id, session=session
            )
        db_picnic.users = users

    return db_picnic
