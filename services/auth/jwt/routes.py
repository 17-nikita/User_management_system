# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from services.users.models import User
# from core.database.session import get_db
# from services.auth.jwt.service import create_access_token
# from core.common.utils import hash_password, verify_password
# from services.auth.jwt.schemas import SignupRequest, LoginRequest

# router = APIRouter(prefix="/auth", tags=["Authentication"])

# @router.post("/signup")
# def signup(request: SignupRequest, db: Session = Depends(get_db)):
#     if db.query(User).filter(User.email == request.email).first():
#         raise HTTPException(status_code=400, detail="Email already registered")
    
#     user = User(
#         username=request.username,
#         email=request.email,
#         hashed_password=hash_password(request.password)
#     )
#     db.add(user)
#     db.commit()
#     db.refresh(user)

#     token = create_access_token({"sub": user.email})
#     return {"access_token": token}

# @router.post("/login")
# def login(request: LoginRequest, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.email == request.email).first()
#     if not user or not verify_password(request.password, user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token({"sub": user.email})
#     return {"access_token": token}



# services/auth/jwt/routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.users.models import User
from core.database.session import get_db
from services.auth.jwt.service import create_access_token
from core.common.utils import hash_password, verify_password
from services.auth.jwt.schemas import SignupRequest, LoginRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == request.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user = User(
        username=request.username,
        email=request.email,
        hashed_password=hash_password(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(subject=user.email)
    return {"access_token": token}

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(subject=user.email)
    return {"access_token": token}

