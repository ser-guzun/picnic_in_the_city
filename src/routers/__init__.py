from fastapi import APIRouter

from src.routers import city, picnic

router = APIRouter()

router.include_router(city.router, prefix="/city")
router.include_router(picnic.router, prefix="/picnic")
