import os

from pydantic_settings import BaseSettings

def get_env_file():
    return os.environ.get('.env')

class Settings(BaseSettings):
    IS_PRODUCT: bool
    SERVER_UUID: str
    ALGORITHM: str

    APPLE_PRIVACY_KEY: str
    APPLE_TEAM_ID: str
    APPLE_KEY_ID: str

    class Config:
        env_file = get_env_file()

