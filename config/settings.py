import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BACKEND_BASE_URL: str = os.getenv("BACKEND_BASE_URL", "http://localhost:8000")
    MOCK_MODE: bool = os.getenv("MOCK_MODE", "true").lower() == "true"
    APP_ENV: str = os.getenv("APP_ENV", "development")

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()
