import requests
from account.serializers import FriendRequestSerializer, UserSerializer
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from utils.constant import API_RESPONSE_OBJ, RESPONSE_MSG_API, RESPONSE_STATUS_API
from utils.environment import BASE_URL

from .forms import SigupForm, UserDetailsForm
from .models import FriendRequest, FriendRequestStatus, User


@api_view(["GET"])
def user_details(request):
    """This function fetches User Details.

    Args:
        request (object): contains request details

    Returns:
        response(dict): user details and status of operation
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        user = User.objects.get(id=request.user.id)
        if not user:
            response[RESPONSE_MSG_API] = "User does not exist."
            return JsonResponse(response)
        response["payload"] = UserSerializer(user).data
        if response["payload"]:
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "User details fetched."
    except Exception as ex:
        print(f"Error api_view.conversation_list: {ex}")
    return JsonResponse(response)


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    """This function creates User

    Args:
        request (object): contains request details

    Returns:
        JsonResponse(dict): status of operation
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        data = request.data
        form = SigupForm(
            {
                "email": data.get("email"),
                "name": data.get("name"),
                "password1": data.get("password"),
                "password2": data.get("confirm_password"),
            }
        )
        if form.is_valid():
            form.save()
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "User created successfully."
            # send verfication email later!
    except Exception as ex:
        print(f"Error api_view.signup: {ex}")
    return JsonResponse(response)


@api_view(["POST"])
def user_details_update(request, pk):
    """This function updates User

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        JsonResponse(dict): status of operation
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        data = request.data
        user = User.objects.get(pk=request.user.id)
        if user:
            if request.user.id == pk:
                if user.check_password(data.get("current_password")):
                    form = UserDetailsForm(
                        request.data or None, request.FILES, instance=user
                    )
                    if data.get("password1", None) and data.get("password2", None):
                        password_form = PasswordChangeForm(
                            user,
                            {
                                "old_password": data["current_password"],
                                "new_password1": data["password1"],
                                "new_password2": data["password2"],
                            },
                        )
                        if password_form.is_valid() and form.is_valid():
                            user.set_password(data["password1"])
                            user.save()
                            form.save()
                            update_session_auth_hash(request, user)
                            response[RESPONSE_STATUS_API] = True
                            response[
                                RESPONSE_MSG_API
                            ] = "User details updated successfully."
                    else:
                        if form.is_valid():
                            form.save()
                            response[RESPONSE_STATUS_API] = True
                            response[
                                RESPONSE_MSG_API
                            ] = "User details updated successfully."
                else:
                    response[RESPONSE_MSG_API] = "Entered incorrect current password."
            else:
                response[RESPONSE_MSG_API] = "Entered incorrect details."
    except Exception as ex:
        print(f"Error api_view.user_details_update: {ex}")
    return JsonResponse(response)


@api_view(["GET"])
def friends(request, pk):
    """This function fetches list of friends

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        JsonResponse(dict): status of operation and friends details
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        user = User.objects.get(pk=pk)
        if user:
            friend_requests = []
            response["payload"] = {}
            if user == request.user:
                friend_requests = FriendRequest.objects.filter(
                    created_for=request.user, status=FriendRequestStatus.SENT.value
                )
                response["payload"]["requests"] = FriendRequestSerializer(
                    friend_requests, many=True
                ).data
            all_friends = user.friends.all()
            response["payload"]["user"] = UserSerializer(user).data
            response["payload"]["friends"] = UserSerializer(all_friends, many=True).data
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "Friends details fetched successfully."
    except Exception as ex:
        print(f"Error api_view.friends: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["POST"])
def send_friend_request(request, pk):
    """This function send's friend request

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        JsonResponse(dict): status of operation
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        user = User.objects.get(pk=pk)
        if user:
            existing_request = FriendRequest.objects.filter(
                (Q(created_for=request.user) & Q(created_by=user))
                | (Q(created_for=user) & Q(created_by=request.user))
            ).first()
            if existing_request:
                if existing_request.status == FriendRequestStatus.REJECTED.value:
                    if existing_request.rejection_count > 3:
                        response[
                            RESPONSE_MSG_API
                        ] = "Friend request rejected more than 3 times. Limit reached."
                    else:
                        existing_request.status = FriendRequestStatus.SENT.value
                        existing_request.rejection_count += 1
                        existing_request.save()
                        response[RESPONSE_MSG_API] = "Friend request sent."
                        response[RESPONSE_STATUS_API] = True
                else:
                    response[RESPONSE_MSG_API] = "Friend request already sent."
            else:
                new_request = FriendRequest.objects.create(
                    created_for=user, created_by=request.user
                )
                new_request.save()
                response[RESPONSE_MSG_API] = "Friend request sent."
                response[RESPONSE_STATUS_API] = True
    except Exception as ex:
        print(f"Error api_view.send_friend_request: {ex}")
    return JsonResponse(response)


@api_view(["POST"])
def handle_friend_request(request, pk, status):
    """This function handle's the friend request

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user
        status (str): status of the friend request

    Returns:
        JsonResponse(dict): status of operation
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        user = User.objects.get(pk=pk)
        if user:
            friend_request = FriendRequest.objects.filter(created_for=request.user).get(
                created_by=user
            )
            if friend_request:
                if status == FriendRequestStatus.ACCEPTED.name:
                    url = f"{BASE_URL}/api/chat/{pk}/get-or-create/"
                    chat_response = requests.post(
                        url, headers=request.headers, data=request.data
                    )
                    if chat_response.status_code == 200:
                        friend_request.status = FriendRequestStatus.ACCEPTED.value
                        user.friends.add(request.user)
                        user.friends_count += 1
                        request_user = request.user
                        request_user.friends_count += 1
                        friend_request.rejection_count = 0
                        user.save()
                        request_user.save()
                    else:
                        return JsonResponse(response)
                else:
                    friend_request.status = FriendRequestStatus.REJECTED.value
                friend_request.save()
                response[RESPONSE_MSG_API] = f"Friend Request {status}"
                response[RESPONSE_STATUS_API] = True
    except Exception as ex:
        print(f"Error api_view.handle_friend_request: {ex}")
    return JsonResponse(response)
