from secrets import token_hex

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Squash App API"
    VERSION: str = "3.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = "../../.env"


settings = Settings()
