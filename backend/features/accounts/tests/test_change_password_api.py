from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from features.accounts.infrastructure.persistence.models.user_model import User


class ChangePasswordAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="change_password@example.com",
            user_name="change_password_user",
            password="OldPassword123!",
        )
        self.url = reverse("accounts_api:user-change-password")

    def test_unauthenticated_request_is_rejected(self):
        response = self.client.post(
            self.url,
            {
                "current_password": "OldPassword123!",
                "new_password": "NewPassword456!",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_authenticated_user_changes_password(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            self.url,
            {
                "current_password": "OldPassword123!",
                "new_password": "NewPassword456!",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("NewPassword456!"))
        self.assertFalse(self.user.check_password("OldPassword123!"))

    def test_incorrect_current_password_is_rejected(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            self.url,
            {
                "current_password": "IncorrectPassword!",
                "new_password": "NewPassword456!",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("OldPassword123!"))