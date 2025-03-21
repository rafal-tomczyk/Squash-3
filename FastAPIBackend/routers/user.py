from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from db.schemas.user import UserCreate, User as UserSchema

router = APIRouter()

@router.post("/users/", response_model=UserSchema)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
