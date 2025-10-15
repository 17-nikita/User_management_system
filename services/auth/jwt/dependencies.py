# services/auth/jwt/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.auth.jwt.service import decode_access_token
from sqlalchemy.orm import Session
from core.database.session import get_db
from services.users.models import User

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security),
                     db: Session = Depends(get_db)) -> User:
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    sub = payload.get("sub")
    if not sub:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    # If subject is email:
    user = db.query(User).filter(User.email == str(sub)).first()
    # If you prefer using user id: cast and query by User.id instead.

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user
