from django.test import TestCase

from features.accounts.application.use_cases.change_password import (
    ChangePassword,
)
from features.accounts.infrastructure.persistence.models.user_model import User
from features.accounts.infrastructure.persistence.repositories.django_user_repository import (
    DjangoUserRepository,
)


class ChangePasswordTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="password_test@example.com",
            user_name="password_test_user",
            password="OldPassword123!",
        )
        self.use_case = ChangePassword(DjangoUserRepository())

    def test_changes_password_successfully(self):
        result = self.use_case.execute(
            self.user.id,
            "OldPassword123!",
            "NewPassword123!",
        )

        self.assertTrue(result)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("NewPassword123!"))
        self.assertFalse(self.user.check_password("OldPassword123!"))

    def test_rejects_incorrect_current_password(self):
        result = self.use_case.execute(
            self.user.id,
            "WrongPassword123!",
            "NewPassword123!",
        )

        self.assertFalse(result)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("OldPassword123!"))

    def test_returns_false_for_nonexistent_user(self):
        from uuid import uuid4

        result = self.use_case.execute(
            uuid4(),
            "OldPassword123!",
            "NewPassword123!",
        )

        self.assertFalse(result)