from uuid import uuid4

from features.accounts.application.interfaces.user_repository import UserRepository
from features.accounts.domain.entities.user import User


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, user_name: str) -> User:
        user = User(
            id=uuid4(),
            email=email,
            user_name=user_name,
        )

        return self.user_repository.create(user)
