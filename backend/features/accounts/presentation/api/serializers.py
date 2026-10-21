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