from unittest import TestCase
from uuid import uuid4

from features.accounts.application.use_cases.get_user_by_id import GetUserById
from features.accounts.domain.entities.user import User


class FakeUserRepository:
    def __init__(self):
        self.users = {}

    def get_by_id(self, user_id):
        return self.users.get(user_id)


class GetUserByIdTests(TestCase):
    def setUp(self):
        self.repository = FakeUserRepository()
        self.use_case = GetUserById(self.repository)

        self.user = User(
            id=uuid4(),
            email="test@example.com",
            user_name="test_user",
        )
        self.repository.users[self.user.id] = self.user

    def test_returns_user_when_found(self):
        result = self.use_case.execute(self.user.id)

        self.assertEqual(result, self.user)

    def test_returns_none_when_user_not_found(self):
        result = self.use_case.execute(uuid4())

        self.assertIsNone(result)