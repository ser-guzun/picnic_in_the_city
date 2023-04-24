from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.dependencies.database import get_session
from src.routers import city, picnic, user
from src.services import logging_service
from src.settings import settings

logging_service.setup_logger(settings.LOGGER_NAME, settings.LOG_FILE, settings)
logging_service.setup_logger(
    "sqlalchemy", f"sqlalchemy_{settings.LOG_FILE}", settings
)

app = FastAPI(dependencies=[Depends(get_session)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(city.router)
app.include_router(picnic.router)
app.include_router(user.router)
