from uuid import UUID

from django.db import transaction

from features.accounts.application.interfaces.user_repository import UserRepository
from features.accounts.domain.entities.user import User as UserEntity
from features.accounts.infrastructure.persistence.models.user_model import User as UserModel


class DjangoUserRepository(UserRepository):

    @staticmethod
    def _to_entity(user_model: UserModel) -> UserEntity:
        return UserEntity(
            id=user_model.id,
            email=user_model.email,
            user_name=user_model.user_name,
            is_active=user_model.is_active,
        )

    @staticmethod
    def _to_model_data(user: UserEntity) -> dict:
        return {
            "id": user.id,
            "email": user.email,
            "user_name": user.user_name,
            "is_active": user.is_active,
        }

    @transaction.atomic
    def create(self, user: UserEntity) -> UserEntity:
        user_model = UserModel.objects.create(**self._to_model_data(user))
        return self._to_entity(user_model)

    def get_by_id(self, user_id: UUID) -> UserEntity | None:
        user_model = UserModel.objects.filter(id=user_id).first()

        if user_model is None:
            return None

        return self._to_entity(user_model)

    def get_by_email(self, email: str) -> UserEntity | None:
        user_model = UserModel.objects.filter(email=email).first()

        if user_model is None:
            return None

        return self._to_entity(user_model)

    @transaction.atomic
    def update(self, user: UserEntity) -> UserEntity:
        user_model = UserModel.objects.get(id=user.id)

        user_model.email = user.email
        user_model.user_name = user.user_name
        user_model.is_active = user.is_active

        user_model.save(
            update_fields=["email", "user_name", "is_active"]
        )

        return self._to_entity(user_model)

    @transaction.atomic
    def delete(self, user_id: UUID) -> None:
        UserModel.objects.filter(id=user_id).delete()
