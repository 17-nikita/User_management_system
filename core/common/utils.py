# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password[:72])

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password[:72], hashed_password)

# from fastapi import Depends, HTTPException, status
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from services.auth.jwt.service import decode_access_token
# from sqlalchemy.orm import Session
# from services.users.models import User
# from core.database.session import get_db

# security = HTTPBearer()

# def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
#     token = credentials.credentials
#     payload = decode_access_token(token)
#     if not payload:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
#     email = payload["sub"]
#     user = db.query(User).filter(User.email == email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return user



# core/common/utils.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # bcrypt limit is 72 bytes — truncate safely
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password[:72], hashed_password)
