
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database.session import get_db
from services.auth.jwt.schemas import SignupRequest, LoginRequest,RefreshRequest
from services.auth.jwt.service import auth_service  # import the service instance

router = APIRouter(prefix="/api/auth/v1", tags=["Authentication"])


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    return auth_service.register_user(db, request)


@router.post("/login", status_code=status.HTTP_200_OK)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return auth_service.authenticate_user(db, request)


@router.post("/refresh")
def refresh_token(request: RefreshRequest):
    return auth_service.refresh_tokens(request.refresh_token)