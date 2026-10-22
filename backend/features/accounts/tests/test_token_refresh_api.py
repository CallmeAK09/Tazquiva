from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


from features.accounts.infrastructure.persistence.models.user_model import User


class TokenRefreshAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="refresh@example.com",
            user_name="refresh_user",
            password="StrongPassword123!",
        )
        self.url = reverse("accounts_api:token-refresh")
        self.refresh_token = str(RefreshToken.for_user(self.user))

    def test_valid_refresh_token_returns_new_access_token(self):
        response = self.client.post(
            self.url,
            {"refresh": self.refresh_token},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_invalid_refresh_token_is_rejected(self):
        response = self.client.post(
            self.url,
            {"refresh": "invalid.refresh.token"},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_expired_refresh_token_is_rejected(self):
        refresh = RefreshToken.for_user(self.user)
        refresh.set_exp(lifetime=timedelta(seconds=-1))

        response = self.client.post(
            self.url,
            {"refresh": str(refresh)},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_missing_refresh_token_is_rejected(self):
        response = self.client.post(
            self.url,
            {},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )