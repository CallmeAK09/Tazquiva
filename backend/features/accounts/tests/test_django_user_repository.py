from uuid import uuid4

from django.test import TestCase

from features.accounts.domain.entities.user import User as UserEntity
from features.accounts.infrastructure.persistence.repositories.django_user_repository import (
    DjangoUserRepository,
)
from features.accounts.infrastructure.persistence.models.user_model import User as UserModel


class DjangoUserRepositoryTests(TestCase):

    def setUp(self):
        self.repository = DjangoUserRepository()
        self.user = UserEntity(
            id=uuid4(),
            email="test@example.com",
            user_name="test_user",
        )

    def test_create_user(self):
        created_user = self.repository.create(self.user)

        self.assertEqual(created_user.id, self.user.id)
        self.assertEqual(created_user.email, self.user.email)
        self.assertEqual(created_user.user_name, self.user.user_name)

    def test_get_by_id_returns_user(self):
        self.repository.create(self.user)

        retrieved_user = self.repository.get_by_id(self.user.id)

        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.id, self.user.id)

    def test_get_by_id_returns_none_for_missing_user(self):
        self.assertIsNone(self.repository.get_by_id(uuid4()))

    def test_get_by_email_returns_user(self):
        self.repository.create(self.user)

        retrieved_user = self.repository.get_by_email(self.user.email)

        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.id, self.user.id)

    def test_get_by_email_returns_none_for_missing_user(self):
        self.assertIsNone(
            self.repository.get_by_email("missing@example.com")
        )

    def test_update_user(self):
        self.repository.create(self.user)

        updated_user = UserEntity(
            id=self.user.id,
            email="updated@example.com",
            user_name="updated_user",
            is_active=False,
        )

        result = self.repository.update(updated_user)

        self.assertEqual(result.email, "updated@example.com")
        self.assertEqual(result.user_name, "updated_user")
        self.assertFalse(result.is_active)

        stored_user = UserModel.objects.get(id=self.user.id)
        self.assertEqual(stored_user.email, "updated@example.com")
        self.assertFalse(stored_user.is_active)

    def test_delete_user(self):
        self.repository.create(self.user)

        self.repository.delete(self.user.id)

        self.assertFalse(
            UserModel.objects.filter(id=self.user.id).exists()
        )
