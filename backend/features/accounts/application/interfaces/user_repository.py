from abc import ABC, abstractmethod
from uuid import UUID

from features.accounts.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        pass

    @abstractmethod
    def change_password(self, user_id: UUID, current_password: str, new_password: str ) -> bool:
        pass