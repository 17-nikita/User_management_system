# services/users/service.py
from typing import Dict, Any
from sqlalchemy.orm import Session
from services.users.models import User
from services.users.profile.models import Profile
from services.users.schemas import UserUpdate
from core.common.exceptions import not_found, internal_server_error
from core.common.utils import hash_password
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


 

    def update_current_user(self,db: Session, user: User, updates: UserUpdate) -> Dict:
        updates_dict = updates.dict(exclude_unset=True)

        # Handle password separately
        if "password" in updates_dict:
            updates_dict["hashed_password"] = hash_password(updates_dict.pop("password"))

        # Uniqueness checks
        if "username" in updates_dict:
            if db.query(User).filter(User.username == updates_dict["username"], User.id != user.id).first():
                raise internal_server_error()
        if "email" in updates_dict:
            if db.query(User).filter(User.email == updates_dict["email"], User.id != user.id).first():
                raise internal_server_error()

        if updates_dict:
            try:
                db.query(User).filter(User.id == user.id).update(updates_dict)
                db.commit()
                db.refresh(user)
            except Exception as e:
                db.rollback()
                raise internal_server_error(str(e))
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "message": "User updated successfully"
        }

        

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
