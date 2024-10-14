from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.use_cases.user_service import UserService
from app.adapters.api.models.user import User
from app.adapters.repositories.user_repository import UserRepositoryImpl
from app.adapters.db.database import get_db


router = APIRouter()


async def get_user_service(db: Session = Depends(get_db)):
    user_repo = UserRepositoryImpl(db)
    return UserService(user_repo)


@router.get("/users/{user_id}")
def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users")
def create_user(user: User, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user)