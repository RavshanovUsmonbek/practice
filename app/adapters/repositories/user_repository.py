from sqlalchemy.future import select
from typing import Optional
from app.core.ports.repositories.user_repository import UserRepository
from app.core.domain.user import User
from app.adapters.db.models.user import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self, session):
        self.session = session

    def get_user(self, user_id: int) -> Optional[User]:
        user_model = self.session.query(UserModel).filter(UserModel.user_id == user_id).first()
        if user_model:
            return User(user_id=user_model.user_id, username=user_model.username, email=user_model.email)
        return None

    def create_user(self, user: User) -> User:
        user_model = UserModel(user_id=user.user_id, username=user.username, email=user.email)
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        return User(user_id=user_model.user_id, username=user_model.username, email=user_model.email)



