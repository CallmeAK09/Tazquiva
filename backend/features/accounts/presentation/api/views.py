from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from features.accounts.application.use_cases.change_password import ChangePassword
from features.accounts.application.use_cases.create_user import CreateUser
from features.accounts.application.use_cases.delete_user import DeleteUser
from features.accounts.application.use_cases.get_user_by_id import GetUserById
from features.accounts.application.use_cases.login_user import LoginUser
from features.accounts.application.use_cases.update_user import UpdateUser
from features.accounts.domain.entities.user import User
from features.accounts.infrastructure.persistence.models.user_model import (
    User as UserModel,
)
from features.accounts.infrastructure.persistence.repositories.django_user_repository import (
    DjangoUserRepository,
)
from features.accounts.presentation.api.serializers import (
    ChangePasswordSerializer,
    CreateUserSerializer,
    LoginSerializer,
    UpdateUserSerializer,
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


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def get_user_by_id(request, user_id):
    user_repository = DjangoUserRepository()
    get_user_use_case = GetUserById(user_repository)

    user = get_user_use_case.execute(user_id)

    if user is None:
        return Response(
            {"detail": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method in ["PUT", "PATCH"]:
        serializer = UpdateUserSerializer(
            data=request.data,
            context={"user_id": user_id},
        )

        serializer.is_valid(raise_exception=True)

        if request.method == "PUT":
            required_fields = ["email", "user_name"]
            missing_fields = [
                field
                for field in required_fields
                if field not in serializer.validated_data
            ]

            if missing_fields:
                return Response(
                    {
                        field: ["This field is required."]
                        for field in missing_fields
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        updated_user = User(
            id=user.id,
            email=serializer.validated_data.get("email", user.email),
            user_name=serializer.validated_data.get(
                "user_name",
                user.user_name,
            ),
            is_active=serializer.validated_data.get(
                "is_active",
                user.is_active,
            ),
        )

        update_use_case = UpdateUser(user_repository)
        updated_user = update_use_case.execute(updated_user)

        response_serializer = UserSerializer(updated_user)

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK,
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    use_case = ChangePassword(DjangoUserRepository())

    success = use_case.execute(
        user_id=request.user.id,
        current_password=serializer.validated_data["current_password"],
        new_password=serializer.validated_data["new_password"],
    )

    if not success:
        return Response(
            {"current_password": ["Current password is incorrect."]},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(
        {"detail": "Password changed successfully."},
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    use_case = LoginUser(DjangoUserRepository())
    user = use_case.execute(
        email=serializer.validated_data["email"],
        password=serializer.validated_data["password"],
    )

    if user is None:
        return Response(
            {"detail": "Invalid email or password."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    refresh = RefreshToken.for_user(
        UserModel.objects.get(id=user.id)
    )

    return Response(
        {
            "user": UserSerializer(user).data,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        },
        status=status.HTTP_200_OK,
    )