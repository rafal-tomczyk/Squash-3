from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Squash3"
    DB_CONNECTION_LINK: str
    class Config:
        env_file = ".env"
