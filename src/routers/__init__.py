from fastapi import APIRouter
from src.routers import city

router = APIRouter()

router.include_router(city.router, prefix='/city')
