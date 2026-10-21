from uuid import UUID

from features.accounts.application.interfaces.user_repository import UserRepository
from features.accounts.domain.entities.user import User


class GetUserById:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: UUID) -> User | None:
        return self.user_repository.get_by_id(user_id)