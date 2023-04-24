import os
from pathlib import Path

import pydantic
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class LoggingSettingsMixin(pydantic.BaseSettings):
    LOGGER_NAME: str = "src"
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = (
        "%(asctime)s %(levelname)s func:%(funcName)s %(name)s %(message)s"
    )
    LOG_PATH: str = "../data/logs/"
    LOG_FILE: str = "py_log"


class SettingsBase:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


class Settings(SettingsBase, LoggingSettingsMixin):
    pass


settings: Settings = Settings()
