from abc import ABC, abstractmethod
from ..models.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        pass
