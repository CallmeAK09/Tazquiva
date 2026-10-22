from features.accounts.application.interfaces.user_repository import UserRepository
from features.accounts.domain.entities.user import User


class LoginUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> User | None:
        return self.user_repository.authenticate(email, password)