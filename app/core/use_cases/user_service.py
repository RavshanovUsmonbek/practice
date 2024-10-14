from inspect import iscoroutine, isawaitable
from typing import Optional, Union
from app.core.domain.user import User
from app.core.ports.repositories.user_repository import UserRepository, UserRepositoryAsync


class UserService:
    def __init__(self, user_repository: Union[UserRepository, UserRepositoryAsync]):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_user(user_id)

    def create_user(self, user: User) -> User:
        return self.user_repository.create_user(user)
