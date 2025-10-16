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
   

# Schema for returning user in responses
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    message: str
    class Config:
        from_attributes = True
