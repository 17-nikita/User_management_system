# services/users/service.py
from typing import Dict, Any
from sqlalchemy.orm import Session
from services.users.models import User
from services.users.profile.models import Profile
from services.users.schemas import UserUpdate
from core.common.exceptions import not_found, internal_server_error

class UserService:

    def get_current_user_info(self, user: User) -> Dict[str, Any]:
        """
        Return user info with success message.
        """
        if not user:
            raise not_found("User not found")
        return {
            "message": f"User '{user.username}' retrieved successfully",
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

    def update_current_user(self, db: Session, user: User, updates: UserUpdate) -> Dict[str, Any]:
        try:
            for field, value in updates.dict(exclude_unset=True).items():
                setattr(user, field, value)
            db.commit()
            db.refresh(user)
            return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "message": f"User '{user.username}' updated successfully"
        }
        except Exception as e:
            raise internal_server_error(str(e))
        

    def delete_current_user(self, db: Session, user: User) -> Dict[str, Any]:
        try:
            if not user:
                raise not_found("User not found")
            if user.profile:
                db.delete(user.profile)
            db.delete(user)
            db.commit()
            return {"message": f"User '{user.username}' deleted successfully"}
        except Exception as e:
            raise internal_server_error(str(e))



user_service = UserService()
