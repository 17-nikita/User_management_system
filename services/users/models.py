
# services/users/models.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from core.connections.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(120), unique=True)
    hashed_password = Column(String(128))
    is_active = Column(Boolean, default=True)

    # one-to-one relationship: ORM will delete orphaned Profile objects
    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
        passive_deletes=True,  # rely on DB ON DELETE CASCADE for raw SQL deletes
    )

