from fastapi import FastAPI, Depends

from src.dependencies.database import get_db
from src.routers import city

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(city.router)
