

# core/common/utils.py
from passlib.context import CryptContext

# services/auth/jwt/service.py
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from typing import Any, Dict
from core.config import settings


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    # bcrypt limit is 72 bytes — truncate safely
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password[:72], hashed_password)



def create_access_token(subject: str, extra_claims: Dict[str, Any] | None = None) -> str:
    """
    subject: user identifier (email or str(id))
    """
    now = datetime.utcnow()
    payload: Dict[str, Any] = {
        "sub": str(subject),
        "iat": now,
        "exp": now + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)),
    }
    if extra_claims:
        payload.update(extra_claims)
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_access_token(token: str) -> Dict[str, Any] | None:
    """
    Return payload dict if valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload if "sub" in payload else None
    except ExpiredSignatureError:
        return None
    except JWTError:
        return None
