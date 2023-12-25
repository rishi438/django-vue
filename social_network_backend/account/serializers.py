from rest_framework import serializers

from .models import FriendRequest, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "friends_count",
        )


class FriendRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "created_by",
        )
