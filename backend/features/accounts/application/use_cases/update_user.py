from features.accounts.application.interfaces.user_repository import UserRepository
from features.accounts.domain.entities.user import User


class UpdateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user: User) -> User:
        return self.user_repository.update(user)