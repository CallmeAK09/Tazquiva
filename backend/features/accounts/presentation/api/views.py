from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from features.accounts.application.use_cases.get_user_by_id import GetUserById
from features.accounts.infrastructure.persistence.repositories.django_user_repository import (
    DjangoUserRepository,
)
from features.accounts.presentation.api.serializers import UserSerializer


@api_view(["GET"])
def get_user_by_id(request, user_id):
    user_repository = DjangoUserRepository()
    use_case = GetUserById(user_repository)

    user = use_case.execute(user_id)

    if user is None:
        return Response(
            {"detail": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = UserSerializer(user)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )