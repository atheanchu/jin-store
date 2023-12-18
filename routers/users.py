from fastapi import APIRouter, Depends
from utils.database import get_session
from models.user import User
from sqlmodel import Session

user_router = APIRouter(prefix="/users")


@user_router.get("/")
async def get_users(db: Session = Depends(get_session)):
    users = db.query(User).order_by(User.username.asc()).all()
    db.close()
    return users
