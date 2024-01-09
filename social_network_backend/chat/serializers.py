from account.serializers import UserSerializer
from rest_framework import serializers

from .models import Conversation, ConversationMessage


class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True)

    class Meta:
        model = Conversation
        fields = (
            "id",
            "users",
            "modified_at_formatted",
        )


class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = ConversationSerializer(read_only=True)
    created_by = ConversationSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = (
            "id",
            "sent_to",
            "created_by",
            "created_at_formatted",
            "body",
        )


class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = (
            "id",
            "users",
            "modified_at_formatted",
            "messages",
        )
