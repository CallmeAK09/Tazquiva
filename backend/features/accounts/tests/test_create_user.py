from unittest import TestCase
from uuid import UUID

from features.accounts.application.use_cases.create_user import CreateUser
from features.accounts.domain.entities.user import User


class FakeUserRepository:
    def __init__(self):
        self.created_user = None

    def create(self, user: User) -> User:
        self.created_user = user
        return user


class CreateUserTests(TestCase):
    def setUp(self):
        self.repository = FakeUserRepository()
        self.use_case = CreateUser(self.repository)

    def test_creates_user_with_generated_uuid(self):
        user = self.use_case.execute(
            email="test@example.com",
            user_name="test_user",
        )

        self.assertIsInstance(user.id, UUID)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.user_name, "test_user")
        self.assertTrue(user.is_active)

    def test_persists_user_through_repository(self):
        user = self.use_case.execute(
            email="test@example.com",
            user_name="test_user",
        )

        self.assertIs(self.repository.created_user, user)
