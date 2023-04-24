from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import PicnicUser


async def registration_user_to_picnic(
    picnic_id: int, user_id: int, session: AsyncSession
) -> PicnicUser:
    picnic_user = PicnicUser(picnic_id=picnic_id, user_id=user_id)
    session.add(picnic_user)
    await session.commit()
    return picnic_user


async def get_users_by_picnic_id(
    picnic_id: int, session: AsyncSession
) -> list[PicnicUser]:
    picnic_users = await session.execute(
        select(PicnicUser).where(PicnicUser.picnic_id == picnic_id)
    )
    return picnic_users.scalars().all()
