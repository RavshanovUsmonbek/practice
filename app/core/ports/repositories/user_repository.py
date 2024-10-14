from typing import Optional
from app.core.domain.user import User
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass


class UserRepositoryAsync(ABC):
    @abstractmethod
    async def get_user(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

