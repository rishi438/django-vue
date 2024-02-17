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

from .forms import SigupForm, UserDetailsForm
from .models import FriendRequest, FriendRequestStatus, User


@api_view(["GET"])
def me(request):
    """User Details fetch

    Args:
        request (object): contains request details

    Returns:
        response(dict): return data and status
    """
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "email": request.user.email,
            "friends_count": request.user.friends_count,
            "posts_count": request.user.posts_count,
        }
    )


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    """User creation function

    Args:
        request (object): contains request details

    Returns:
        response(dict): return data and status
    """
    data = request.data
    message = "User created successfully!"
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
        # send verfication email later!
    else:
        message = "Error occurred please contact Tech Team!"
    return JsonResponse({"msg": message})


@api_view(["POST"])
def user_details_update(request, pk):
    data = request.data
    user = User.objects.get(pk=request.user.id)
    message = ""
    if request.user.id == pk:
        if user.check_password(data["current_password"]):
            form = UserDetailsForm(request.data or None, request.FILES, instance=user)
            if data["password1"] and data["password2"]:
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
                    message = "User details updated successfully!"
                else:
                    message = "Error occurred, please contact the Tech Team!"
            else:
                if form.is_valid():
                    form.save()
                    message = "User details updated successfully!"
                else:
                    message = "Error occurred, please contact the Tech Team!"
        else:
            message = "Entered incorrect current password!"
    else:
        message = "Entered incorrect details!"
    return JsonResponse({"msg": message})


@api_view(["GET"])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []
    if user == request.user:
        requests = FriendRequest.objects.filter(
            created_for=request.user, status=FriendRequestStatus.SENT.value
        )
    all_friends = user.friends.all()
    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(all_friends, many=True).data,
            "requests": FriendRequestSerializer(requests, many=True).data,
        },
        safe=False,
    )


@api_view(["POST"])
def send_friend_request(request, pk):
    user = User.objects.get(pk=pk)
    existing_request = FriendRequest.objects.filter(
        (Q(created_for=request.user) & Q(created_by=user))
        | (Q(created_for=user) & Q(created_by=request.user))
    ).first()
    if existing_request:
        if existing_request.status == FriendRequestStatus.REJECTED.value:
            if existing_request.rejection_count > 3:
                return JsonResponse(
                    {"msg": "Friend request rejected more than 3 times. Limit reached."}
                )
            existing_request.status = FriendRequestStatus.SENT.value
            existing_request.rejection_count += 1
            existing_request.save()
            return JsonResponse({"msg": "Friend request sent."})
        return JsonResponse({"msg": "Friend request already sent!"})
    new_request = FriendRequest.objects.create(
        created_for=user, created_by=request.user
    )
    new_request.save()
    return JsonResponse({"msg": "Friend request sent!"})


@api_view(["POST"])
def handle_friend_request(request, pk, status):
    user = User.objects.get(pk=pk)
    friend_request = FriendRequest.objects.filter(created_for=request.user).get(
        created_by=user
    )
    if status == FriendRequestStatus.ACCEPTED.name:
        url = f"http://localhost:8000/api/chat/{pk}/get-or-create/"
        chat_response = requests.post(url, headers=request.headers, data=request.data)
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
        friend_request.status = FriendRequestStatus.REJECTED.value

    friend_request.save()
    return JsonResponse({"msg": f"Friend Request {status}"})
