from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.user_service import create_user, verify_user
from app.auth.auth_handler import create_token
from app.auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserResponse)
def signup(data: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, data.username, data.password)
    return user

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = verify_user(db, data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.username)
    return {"access_token": token}
