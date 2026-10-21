from features.accounts.application.interfaces.user_repository import UserRepository
from features.accounts.domain.entities.user import User


class GetUserByEmail:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str) -> User | None:
        return self.user_repository.get_by_email(email)