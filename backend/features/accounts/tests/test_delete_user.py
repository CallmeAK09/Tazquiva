from unittest import TestCase
from uuid import uuid4

from features.accounts.application.use_cases.delete_user import DeleteUser


class FakeUserRepository:
    def __init__(self):
        self.deleted_user_ids = []

    def delete(self, user_id):
        self.deleted_user_ids.append(user_id)


class DeleteUserTests(TestCase):
    def setUp(self):
        self.repository = FakeUserRepository()
        self.use_case = DeleteUser(self.repository)

    def test_deletes_user_through_repository(self):
        user_id = uuid4()

        self.use_case.execute(user_id)

        self.assertIn(user_id, self.repository.deleted_user_ids)

    def test_execute_returns_none(self):
        result = self.use_case.execute(uuid4())

        self.assertIsNone(result)