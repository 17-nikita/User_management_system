# services/auth/jwt/service.py
from typing import Dict, Any
from sqlalchemy.orm import Session
from services.users.models import User
from services.auth.jwt.schemas import SignupRequest, LoginRequest
from core.common.utils import hash_password, verify_password, create_access_token
from core.common.exceptions import bad_request, unauthorized, internal_server_error

class AuthService:

    def __init__(self, token_subject_field: str = "email"):
        self.token_subject_field = token_subject_field

    def register_user(self, db: Session, payload: SignupRequest) -> Dict[str, Any]:
        """
        Register a new user.
        Raises HTTPExceptions internally for invalid cases.
        Returns a dict with user info for response.
        """
        try:
            existing = db.query(User).filter(User.email == payload.email).first()
            if existing:
                raise bad_request("Email already registered")

            user = User(
                username=payload.username,
                email=payload.email,
                hashed_password=hash_password(payload.password),
            )
            db.add(user)
            db.commit()
            db.refresh(user)

            return {
                "message": f"User '{user.username}' registered successfully",
                "username": user.username,
                "email": user.email
            }
        except Exception as e:
            # Wrap unexpected errors
            raise internal_server_error(str(e))

    def authenticate_user(self, db: Session, payload: LoginRequest) -> Dict[str, Any]:
        """
        Authenticate a user.
        Raises HTTPExceptions internally for invalid credentials or unexpected errors.
        Returns a dict containing message, token, and user info.
        """
        try:
            user = db.query(User).filter(User.email == payload.email).first()
            if not user or not verify_password(payload.password, user.hashed_password):
                raise unauthorized("Invalid email or password")

            subject = getattr(user, self.token_subject_field)
            token = create_access_token(subject=str(subject))

            return {
                "message": f"User '{user.username}' logged in successfully",
                "access_token": token,
                "token_type": "bearer",
                "email": user.email
            }
        except Exception as e:
            raise internal_server_error(str(e))


# Module-level instance for convenience
auth_service = AuthService(token_subject_field="email")
