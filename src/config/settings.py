from typing import Optional
import os
from pydantic import BaseSettings, validator
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()

    @validator("OPENAI_API_KEY")
    def validate_openai_api_key(cls, value):
        if not value:
            raise ValueError("OPENAI_API_KEY environment variable is required.")
        return value

    class Config:
        env_file = ".env"

settings = Settings()