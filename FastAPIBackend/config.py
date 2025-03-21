from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Squash3"
    DB_CONNECTION_LINK: str
    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
