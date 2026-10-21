from rest_framework import serializers

from features.accounts.domain.entities.user import User


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