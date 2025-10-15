# Stores global settings that other parts of the app can use

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env file before using Settings
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str 
    JWT_SECRET_KEY: str 
    JWT_ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings= Settings()


# sqlite:///: Specifies that we're using SQLite.
# ./app.db: Points to a file named app.db in the current working directory (. means the current folder).