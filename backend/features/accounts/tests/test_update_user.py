from unittest import TestCase
from uuid import uuid4

from features.accounts.application.use_cases.update_user import UpdateUser
from features.accounts.domain.entities.user import User


class FakeUserRepository:
    def __init__(self):
        self.updated_user = None

    def update(self, user: User) -> User:
        self.updated_user = user
        return user


class UpdateUserTests(TestCase):
    def setUp(self):
        self.repository = FakeUserRepository()
        self.use_case = UpdateUser(self.repository)

    def test_updates_user_through_repository(self):
        user = User(
            id=uuid4(),
            email="updated@example.com",
            user_name="updated_user",
        )

        self.use_case.execute(user)

        self.assertEqual(self.repository.updated_user, user)

    def test_returns_updated_user(self):
        user = User(
            id=uuid4(),
            email="updated@example.com",
            user_name="updated_user",
        )

        result = self.use_case.execute(user)

        self.assertEqual(result, user)