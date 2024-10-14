import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict



def get_env_file_location():
    root_dir = os.getcwd()
    resource_dir = os.getenv("RESOURCE_DIR", "./config/resources")
    env_file = (
        f"{root_dir}/{resource_dir}/.env."
        + os.getenv("ENVIRONMENT", "local").lower()
    )
    print(f'___________________{env_file}')
    return env_file


class Settings(BaseSettings):
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    DB_HOST: str

    model_config = SettingsConfigDict(
        env_file=get_env_file_location(), env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


def get_clear_cache():
    get_settings().cache_clear()