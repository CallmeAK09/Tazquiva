from unittest import TestCase
from uuid import uuid4

from features.accounts.application.use_cases.get_user_by_email import GetUserByEmail
from features.accounts.domain.entities.user import User


class FakeUserRepository:
    def __init__(self):
        self.users = {}

    def get_by_email(self, email: str) -> User | None:
        return self.users.get(email)


class GetUserByEmailTests(TestCase):
    def setUp(self):
        self.repository = FakeUserRepository()
        self.use_case = GetUserByEmail(self.repository)

        self.user = User(
            id=uuid4(),
            email="test@example.com",
            user_name="test_user",
        )
        self.repository.users[self.user.email] = self.user

    def test_returns_user_when_found(self):
        result = self.use_case.execute("test@example.com")

        self.assertEqual(result, self.user)

    def test_returns_none_when_user_not_found(self):
        result = self.use_case.execute("missing@example.com")

        self.assertIsNone(result)