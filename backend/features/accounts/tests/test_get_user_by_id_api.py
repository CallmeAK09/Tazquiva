from uuid import uuid4

from rest_framework import status
from rest_framework.test import APITestCase

from features.accounts.domain.entities.user import User as UserEntity
from features.accounts.infrastructure.persistence.repositories.django_user_repository import (
    DjangoUserRepository,
)


class GetUserByIdAPITests(APITestCase):

    def setUp(self):
        self.repository = DjangoUserRepository()
        self.user = UserEntity(
            id=uuid4(),
            email="api-test@example.com",
            user_name="api_test_user",
        )
        self.repository.create(self.user)

        self.url = f"/api/accounts/users/{self.user.id}/"

    def test_get_user_by_id_returns_user_details(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": str(self.user.id),
                "email": self.user.email,
                "user_name": self.user.user_name,
                "is_active": True,
            },
        )

    def test_get_user_by_id_returns_404_for_missing_user(self):
        missing_user_id = uuid4()
        url = f"/api/accounts/users/{missing_user_id}/"

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )
        self.assertEqual(response.data["detail"], "User not found.")

    def test_get_user_by_id_returns_404_for_invalid_uuid(self):
        response = self.client.get(
            "/api/accounts/users/not-a-valid-uuid/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )
