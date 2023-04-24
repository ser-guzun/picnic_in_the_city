from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import Picnic
from src.schemas.picnic import PicnicCreate


async def get_picnics(session: AsyncSession) -> list[Picnic]:
    picnics = await session.execute(select(Picnic))
    return picnics.scalars().all()


async def get_picnic_by_id(picnic_id: int, session: AsyncSession) -> Picnic:
    picnic = await session.execute(select(Picnic).where(Picnic.id == picnic_id))
    return picnic.scalar()


async def get_picnics_by_reason(
    picnic_reason: str, session: AsyncSession
) -> list[Picnic]:
    picnics = await session.execute(
        select(Picnic).where(Picnic.name == picnic_reason)
    )
    return picnics.scalars().all()


async def create_picnic(picnic: PicnicCreate, session: AsyncSession) -> Picnic:
    db_picnic = Picnic(
        reason=picnic.reason,
        city_id=picnic.city_id,
        time=picnic.time,
    )
    session.add(db_picnic)
    await session.commit()
    return db_picnic
