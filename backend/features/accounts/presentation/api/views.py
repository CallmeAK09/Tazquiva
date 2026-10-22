from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from features.accounts.application.use_cases.create_user import CreateUser
from features.accounts.application.use_cases.delete_user import DeleteUser
from features.accounts.application.use_cases.get_user_by_id import GetUserById
from features.accounts.infrastructure.persistence.repositories.django_user_repository import (
    DjangoUserRepository,
)
from features.accounts.presentation.api.serializers import (
    CreateUserSerializer,
    UserSerializer,
)


@api_view(["POST"])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    use_case = CreateUser(DjangoUserRepository())
    user = use_case.execute(
        email=serializer.validated_data["email"],
        user_name=serializer.validated_data["user_name"],
    )

    response_serializer = UserSerializer(user)

    return Response(
        response_serializer.data,
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET", "DELETE"])
def get_user_by_id(request, user_id):
    user_repository = DjangoUserRepository()
    get_user_use_case = GetUserById(user_repository)

    user = get_user_use_case.execute(user_id)

    if user is None:
        return Response(
            {"detail": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "DELETE":
        delete_use_case = DeleteUser(user_repository)
        delete_use_case.execute(user_id)

        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = UserSerializer(user)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )