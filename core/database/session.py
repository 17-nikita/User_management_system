from sqlalchemy.orm import sessionmaker
from core.connections.database import engine
#from core.connections.database import SessionLocal  # SQLAlchemy sessionmaker


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
