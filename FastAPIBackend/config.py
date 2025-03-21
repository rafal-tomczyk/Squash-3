from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Squash3"
    DB_CONNECTION_LINK: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
print(settings.DB_CONNECTION_LINK)
test_zmiennej = settings.DB_CONNECTION_LINK
