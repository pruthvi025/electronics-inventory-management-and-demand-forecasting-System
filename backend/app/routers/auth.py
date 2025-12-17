from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserLogin
from app.services.auth_service import authenticate_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
	access_token = authenticate_user(db, credentials.email, credentials.password)
	return {"access_token": access_token, "token_type": "bearer"}
