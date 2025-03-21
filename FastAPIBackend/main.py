from functools import lru_cache

from fastapi import FastAPI
from routers import user

from . import config


app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()

app.include_router(user.router)
