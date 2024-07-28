from code.account.models import User
from code.utils.constant import API_RESPONSE_OBJ, RESPONSE_MSG_API, RESPONSE_STATUS_API

from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .models import Conversation, ConversationMessage
from .serializers import (
    ConversationDetailSerializer,
    ConversationMessageSerializer,
    ConversationSerializer,
)


@api_view(["GET"])
def conversation_list(request):
    """This function fetches list of conversations

    Args:
        request (object): contains request details

    Returns:
        response(dict): status of operation and list of conversations
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        conversations = Conversation.objects.filter(users__in=list([request.user]))
        response["payload"] = ConversationSerializer(conversations, many=True).data
        response[RESPONSE_STATUS_API] = True
        response[RESPONSE_MSG_API] = "Conversation list fetched."
    except Exception as ex:
        print(f"Error api_view.conversation_list: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["GET"])
def conversation_detail(request, pk):
    """This function fetches conversation details

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        response(dict): status of operation and conversation detail
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        conversation = Conversation.objects.filter(users=request.user).get(pk=pk)
        if not conversation:
            return JsonResponse({"msg": "Conversation does not exist"})
        response["payload"] = ConversationDetailSerializer(conversation).data
        response[RESPONSE_STATUS_API] = True
        response[RESPONSE_MSG_API] = "Converations details fetched."
    except Exception as ex:
        print(f"Error api_view.conversation_detail: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["POST"])
def conversation_send_message(request, pk):
    """This function performs sending message operation

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        response(dict): status of operation
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        conversation = Conversation.objects.filter(users__in=list([request.user])).get(
            pk=pk
        )
        for user in conversation.users.all():
            if user != request.user:
                sent_to = user

        conversation_message = ConversationMessage.objects.create(
            conversation=conversation,
            body=request.data.get("body", None),
            created_by=request.user,
            sent_to=sent_to,
        )
        response["payload"] = ConversationMessageSerializer(conversation_message).data
        response[RESPONSE_STATUS_API] = True
        response[RESPONSE_MSG_API] = "Sent message successfully."
    except Exception as ex:
        print(f"Error api_view.conversation_send_message: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["POST"])
def conversation_get_or_create(request, user_pk):
    """This function gets ot creates conversation

    Args:
        request (object): contains request details
        user_pk (uuid): unique id of the specific user

    Returns:
        response(dict): status of operation or conversation details
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        user = User.objects.get(pk=user_pk)
        conversation = Conversation.objects.filter(
            users__in=list([request.user])
        ).filter(users__in=list([user]))
        if conversation.exists():
            conversation = conversation.first()
        else:
            conversation = Conversation.objects.create()
            conversation.users.add(user, request.user)
            conversation.save()
        response["payload"] = ConversationDetailSerializer(conversation).data
        response[RESPONSE_STATUS_API] = True
        response[RESPONSE_MSG_API] = "Conversation created or got."
    except Exception as ex:
        print(f"Error api_view.conversation_get_or_create: {ex}")
    return JsonResponse(response, safe=False)
