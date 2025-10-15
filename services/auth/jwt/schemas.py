
from pydantic import BaseModel, EmailStr, constr

class SignupRequest(BaseModel):
    username: str #constr(min_length=3, max_length=50)
    email: EmailStr
    password: str #constr(min_length=6, max_length=72)  # enforce bcrypt max


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshRequest(BaseModel):
    refresh_token: str