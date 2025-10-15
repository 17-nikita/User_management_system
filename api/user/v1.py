# services/users/routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from services.users.models import User
from services.users.schemas import UserUpdate, UserResponse
from core.database.session import get_current_user, get_db
from services.users.service import user_service

router = APIRouter(prefix="/api/users/v1", tags=["User"])


# Get Current User
@router.get("/me", response_model=UserResponse)
def get_my_user(current_user: User = Depends(get_current_user)):
    return user_service.get_current_user_info(current_user)


# Update Current User
@router.patch("/me", response_model=UserResponse)
def update_my_user(user_update: UserUpdate,current_user: User = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    return user_service.update_current_user(db, current_user, user_update)


# Delete Current User

@router.delete("/me", status_code=status.HTTP_200_OK)
def delete_my_user(current_user: User = Depends(get_current_user),db: Session = Depends(get_db)): 
    return user_service.delete_current_user(db, current_user)
