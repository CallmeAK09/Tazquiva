from rest_framework import status
from rest_framework.test import APITestCase

from features.accounts.infrastructure.persistence.models.user_model import User


class LoginAPITests(APITestCase):
    def setUp(self):
        self.email = "login@example.com"
        self.password = "SecurePass123!"

        self.user = User.objects.create_user(
            email=self.email,
            user_name="loginuser",
            password=self.password,
        )

        self.url = "/api/accounts/login/"

    def test_login_returns_access_and_refresh_tokens(self):
        response = self.client.post(
            self.url,
            {
                "email": self.email,
                "password": self.password,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["user"]["email"], self.email)

    def test_login_fails_with_incorrect_password(self):
        response = self.client.post(
            self.url,
            {
                "email": self.email,
                "password": "WrongPassword123!",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )
        self.assertEqual(
            response.data["detail"],
            "Invalid email or password.",
        )

    def test_login_fails_with_unknown_email(self):
        response = self.client.post(
            self.url,
            {
                "email": "unknown@example.com",
                "password": self.password,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_login_fails_for_inactive_user(self):
        self.user.is_active = False
        self.user.save(update_fields=["is_active"])

        response = self.client.post(
            self.url,
            {
                "email": self.email,
                "password": self.password,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )