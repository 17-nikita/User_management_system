from pydantic import BaseModel, EmailStr
from typing import Optional
from services.users.profile.schemas import ProfileResponse

# Shared fields for users
class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: Optional[bool] = True

# Schema for creating a user
class UserCreate(UserBase):
    password: str  # plain text password (to be hashed before storing)

# Schema for updating a user
class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]

# Schema for returning user in responses
class UserResponse(UserBase):
    id: int
    profile: Optional[ProfileResponse] = None  # nested profile

    class Config:
        from_attributes = True
