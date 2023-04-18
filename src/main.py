from fastapi import Depends, FastAPI

from src.dependencies.database import get_db
from src.routers import city, picnic, user

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(city.router)
app.include_router(picnic.router)
app.include_router(user.router)
