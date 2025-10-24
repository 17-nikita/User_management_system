from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from typing import Any, Dict
from passlib.context import CryptContext
from core.config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


# ---------------- Password ---------------- #
def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password[:72], hashed_password)


# ---------------- JWT (Access + Refresh) ---------------- #
def create_access_token(subject: str, extra_claims: Dict[str, Any] | None = None) -> str:
    now = datetime.utcnow()
    payload: Dict[str, Any] = {
        "sub": str(subject),
        "iat": now,
        "exp": now + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)),
    }
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def create_refresh_token(subject: str, extra_claims: Dict[str, Any] | None = None) -> str:
    now = datetime.utcnow()
    payload: Dict[str, Any] = {
        "sub": str(subject),
        "iat": now,
        "exp": now + timedelta(days=int(settings.REFRESH_TOKEN_EXPIRE_DAYS)),
    }
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(payload, settings.JWT_REFRESH_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> Dict[str, Any] | None:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload if "sub" in payload else None
    except (ExpiredSignatureError, JWTError):
        return None


def decode_refresh_token(token: str) -> Dict[str, Any] | None:
    try:
        payload = jwt.decode(token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload if "sub" in payload else None
    except (ExpiredSignatureError, JWTError):
        return None
