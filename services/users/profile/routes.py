# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from core.database.session import get_db
# from core.common.utils import get_current_user
# from services.users.models import User

# router = APIRouter(prefix="/users", tags=["Users"])

# @router.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     return {
#         "username": current_user.username,
#         "email": current_user.email,
#         "is_active": current_user.is_active
#     }


# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from core.database.session import get_db
# from core.common.utils import get_current_user
# from services.users.profile.models import Profile
# from services.users.profile.models import User
# from services.users.profile.schemas import ProfileCreate, ProfileUpdate, ProfileResponse


# router = APIRouter(prefix="/profiles", tags=["Profiles"])

# # -------------------
# # Create Profile
# # -------------------
# @router.post("/", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
# def create_profile(profile: ProfileCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     if current_user.profile:
#         raise HTTPException(status_code=400, detail="Profile already exists")
#     new_profile = Profile(bio=profile.bio, user_id=current_user.id)
#     db.add(new_profile)
#     db.commit()
#     db.refresh(new_profile)
#     return new_profile

# # -------------------
# # Read Own Profile
# # -------------------
# @router.get("/me", response_model=ProfileResponse)
# def read_my_profile(current_user: User = Depends(get_current_user)):
#     if not current_user.profile:
#         raise HTTPException(status_code=404, detail="Profile not found")
#     return current_user.profile

# # -------------------
# # Update Own Profile
# # -------------------
# @router.patch("/me", response_model=ProfileResponse)
# def update_my_profile(profile_update: ProfileUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     profile = current_user.profile
#     if not profile:
#         raise HTTPException(status_code=404, detail="Profile not found")
#     for field, value in profile_update.dict(exclude_unset=True).items():
#         setattr(profile, field, value)
#     db.commit()
#     db.refresh(profile)
#     return profile

# # -------------------
# # Delete Own Profile
# # -------------------
# @router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
# def delete_my_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     profile = current_user.profile
#     if not profile:
#         raise HTTPException(status_code=404, detail="Profile not found")
#     db.delete(profile)
#     db.commit()
#     return


# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from services.users.models import User, Profile
# from services.users.schemas.user import UserCreate, UserUpdate, UserResponse
# from services.auth.jwt.dependencies import get_current_user, get_db
# from core.common.utils import pwd_context  # if needed

# router = APIRouter(prefix="/users", tags=["Users"])

# # -------------------
# # Get Current User
# # -------------------
# @router.get("/me", response_model=UserResponse)
# def get_my_user(current_user: User = Depends(get_current_user)):
#     return current_user

# # -------------------
# # Update Current User
# # -------------------
# @router.patch("/me", response_model=UserResponse)
# def update_my_user(user_update: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     for field, value in user_update.dict(exclude_unset=True).items():
#         setattr(current_user, field, value)
#     db.commit()
#     db.refresh(current_user)
#     return current_user

# # -------------------
# # Delete Current User
# # -------------------
# @router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
# def delete_my_user(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     # Also delete profile if exists
#     if current_user.profile:
#         db.delete(current_user.profile)
#     db.delete(current_user)
#     db.commit()
#     return



from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.users.models import User
from services.users.profile.models import Profile
from services.users.schemas import UserCreate, UserUpdate, UserResponse
from services.auth.jwt.dependencies import get_current_user
from core.database.session import get_db
from core.common.utils import pwd_context  # if needed

from services.users.profile.schemas import ProfileCreate, ProfileUpdate, ProfileResponse


router = APIRouter(prefix="/profiles", tags=["Profile"])
# -------------------
# Create Profile
# -------------------
@router.post("/profile", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
def create_profile(profile: ProfileCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.profile:
        raise HTTPException(status_code=400, detail="Profile already exists")
    new_profile = Profile(bio=profile.bio, user_id=current_user.id)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

# -------------------
# Read Profile
# -------------------
@router.get("/profile", response_model=ProfileResponse)
def read_my_profile(current_user: User = Depends(get_current_user)):
    if not current_user.profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return current_user.profile

# -------------------
# Update Profile
# -------------------
@router.patch("/profile", response_model=ProfileResponse)
def update_my_profile(profile_update: ProfileUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    profile = current_user.profile
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    for field, value in profile_update.dict(exclude_unset=True).items():
        setattr(profile, field, value)
    db.commit()
    db.refresh(profile)
    return profile

# -------------------
# Delete Profile
# -------------------
@router.delete("/profile", status_code=status.HTTP_204_NO_CONTENT)
def delete_my_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    profile = current_user.profile
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.delete(profile)
    db.commit()
    return
