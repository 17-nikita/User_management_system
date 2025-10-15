from sqlalchemy import create_engine
from core.config import settings
from sqlalchemy.orm import declarative_base

Base=declarative_base()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
