from rest_framework import status
from rest_framework.test import APITestCase

from features.accounts.infrastructure.persistence.models.user_model import (
    User,
)


class CreateUserAPITests(APITestCase):
    url = "/api/accounts/users/"

    def test_create_user_successfully(self):
        payload = {
            "email": "test@example.com",
            "user_name": "testuser",
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], payload["email"])
        self.assertEqual(response.data["user_name"], payload["user_name"])
        self.assertIn("id", response.data)
        self.assertTrue(
            User.objects.filter(email=payload["email"]).exists()
        )

    def test_create_user_with_invalid_email(self):
        payload = {
            "email": "invalid-email",
            "user_name": "testuser",
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_create_user_with_missing_fields(self):
        response = self.client.post(
            self.url,
            {"email": "test@example.com"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("user_name", response.data)

    def test_create_user_with_duplicate_email(self):
        User.objects.create_user(
            email="existing@example.com",
            user_name="existinguser",
        )

        payload = {
            "email": "existing@example.com",
            "user_name": "newuser",
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_create_user_with_duplicate_username(self):
        User.objects.create_user(
            email="duplicate_test@example.com",
            user_name="duplicate_test_user",
        )

        payload = {
            "email": "another_user@example.com",
            "user_name": "duplicate_test_user",
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("user_name", response.data)