from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from features.accounts.infrastructure.persistence.models.user_model import User


class UpdateUserAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="update_test@example.com",
            user_name="update_test_user",
        )
        self.url = reverse(
            "accounts_api:user-detail",
            kwargs={"user_id": self.user.id},
        )

    def test_update_user_successfully(self):
        response = self.client.put(
            self.url,
            {
                "email": "updated@example.com",
                "user_name": "updated_user",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "updated@example.com")
        self.assertEqual(response.data["user_name"], "updated_user")
        self.assertTrue(
            User.objects.filter(
                id=self.user.id,
                email="updated@example.com",
                user_name="updated_user",
            ).exists()
        )

    def test_update_nonexistent_user_returns_404(self):
        from uuid import uuid4

        url = reverse(
            "accounts_api:user-detail",
            kwargs={"user_id": uuid4()},
        )

        response = self.client.put(
            url,
            {
                "email": "updated@example.com",
                "user_name": "updated_user",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_update_user_with_duplicate_email_returns_400(self):
        User.objects.create_user(
            email="existing@example.com",
            user_name="existing_user",
        )

        response = self.client.put(
            self.url,
            {
                "email": "existing@example.com",
                "user_name": "updated_user",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_update_user_with_duplicate_username_returns_400(self):
        User.objects.create_user(
            email="existing@example.com",
            user_name="existing_user",
        )

        response = self.client.put(
            self.url,
            {
                "email": "updated@example.com",
                "user_name": "existing_user",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_update_user_with_invalid_email_returns_400(self):
        response = self.client.put(
            self.url,
            {
                "email": "not-an-email",
                "user_name": "updated_user",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )