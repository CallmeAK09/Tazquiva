from uuid import UUID

from features.accounts.application.interfaces.user_repository import (
    UserRepository,
)


class ChangePassword:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(
        self,
        user_id: UUID,
        current_password: str,
        new_password: str,
    ) -> bool:
        return self.user_repository.change_password(
            user_id=user_id,
            current_password=current_password,
            new_password=new_password,
        )