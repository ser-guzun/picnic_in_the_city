from fastapi import APIRouter

from src.routers import city, picnic, user

router = APIRouter()

router.include_router(city.router)
router.include_router(picnic.router)
router.include_router(user.router)
