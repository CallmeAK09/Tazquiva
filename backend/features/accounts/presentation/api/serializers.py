from rest_framework import serializers

from features.accounts.domain.entities.user import User
from features.accounts.infrastructure.persistence.models.user_model import (
    User as UserModel,
)

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(read_only=True)
    user_name = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def to_representation(self, instance: User) -> dict:
        return {
            "id": str(instance.id),
            "email": instance.email,
            "user_name": instance.user_name,
            "is_active": instance.is_active,
        }

class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    user_name = serializers.CharField(max_length=150)

    def validate_user_name(self, value):
        if UserModel.objects.filter(user_name=value).exists():
            raise serializers.ValidationError(
                "A user with this username already exists."
            )
        return value
    
    def validate_email(self, value):
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value


class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    user_name = serializers.CharField(max_length=150, required=False)
    is_active = serializers.BooleanField(required=False)

    def validate_email(self, value):
        user_id = self.context.get("user_id")

        queryset = UserModel.objects.filter(email=value)

        if user_id:
            queryset = queryset.exclude(id=user_id)

        if queryset.exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )

        return value

    def validate_user_name(self, value):
        user_id = self.context.get("user_id")

        queryset = UserModel.objects.filter(user_name=value)

        if user_id:
            queryset = queryset.exclude(id=user_id)

        if queryset.exists():
            raise serializers.ValidationError(
                "A user with this username already exists."
            )

        return value

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError(
                "At least one field must be provided."
            )

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )
    new_password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
        min_length=8,
    )

    def validate_new_password(self, value):
        from django.contrib.auth.password_validation import validate_password

        validate_password(value)
        return value