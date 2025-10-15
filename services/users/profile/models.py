from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.connections.database import Base

from services.users.models import User

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    full_name=Column(String(50))
    bio = Column(String(255))
    location=Column(String(100))
    mobile_no=Column(String(15))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="profile")