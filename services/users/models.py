from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from core.connections.database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(120), unique=True)
    hashed_password = Column(String(128))
    is_active= Column(Boolean,default=True)
    profile = relationship("Profile", back_populates="user", uselist=False)

