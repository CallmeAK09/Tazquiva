from uuid import uuid4

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from features.accounts.infrastructure.persistence.models.user_model import User


class DeleteUserAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="delete_test@example.com",
            user_name="delete_test_user",
        )
        self.url = reverse(
            "accounts_api:user-detail",
            kwargs={"user_id": self.user.id},
        )

    def test_delete_user_successfully(self):
        response = self.client.delete(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            User.objects.filter(id=self.user.id).exists()
        )

    def test_delete_nonexistent_user(self):
        url = reverse(
            "accounts_api:user-detail",
            kwargs={"user_id": uuid4()},
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )