from fastapi import APIRouter, Depends

from src.dependencies.database import Session, get_db
from src.schemas.picnic import Picnic, PicnicCreate
from src.services import picnic_service

router = APIRouter(dependencies=[Depends(get_db)])


@router.get("/picnics/", response_model=list[Picnic])
def read_picnics(db: Session = Depends(get_db)) -> list[Picnic]:
    return picnic_service.get_picnics(db=db)


@router.get("/picnics/{picnic_id}", response_model=Picnic)
def read_picnic_by_id(picnic_id: int, db: Session = Depends(get_db)) -> Picnic:
    return picnic_service.get_picnic_by_id(picnic_id=picnic_id, db=db)


@router.get("/picnics&q={picnic_reason}", response_model=list[Picnic])
def read_city_by_name(
    picnic_reason: str, db: Session = Depends(get_db)
) -> list[Picnic]:
    return picnic_service.get_picnics_by_reason(picnic_reason=picnic_reason, db=db)


@router.post("/picnics/", response_model=Picnic)
def create_city(picnic: PicnicCreate, db: Session = Depends(get_db)) -> Picnic:
    return picnic_service.create_picnic(picnic=picnic, db=db)
