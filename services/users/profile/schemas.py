from pydantic import BaseModel
from typing import Optional

# Shared fields for profile
class ProfileBase(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    mobile_no: Optional[str] = None

# Schema for creating a profile (user_id required)
class ProfileCreate(ProfileBase):
    user_id: int  # associate profile with a user

# Schema for updating a profile (all fields optional)
class ProfileUpdate(ProfileBase):
    pass  # all fields already optional in ProfileBase

# Schema for returning profile in responses
class ProfileResponse(ProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
