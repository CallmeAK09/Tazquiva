from uuid import UUID

from features.accounts.application.interfaces.user_repository import UserRepository


class DeleteUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: UUID) -> None:
        self.user_repository.delete(user_id)