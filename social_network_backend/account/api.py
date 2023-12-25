from account.serializers import FriendRequestSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)

from .forms import SigupForm
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
    message = "User created successfully"
    form = SigupForm(
        {
            "email": data.get("email"),
            "name": data.get("name"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )
    if form.is_valid():
        form.save()
        # send verfication email later!
    else:
        message = "Error: Invalid Form please contact Tech Team"
    return JsonResponse({"status": message})


@api_view(["GET"])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []
    if user == request.user:
        requests = FriendRequest.objects.filter(
            created_for=request.user,
            status=FriendRequestStatus.SENT.value
        )
    all_friends = user.friends.all()
    return JsonResponse({
        "user": UserSerializer(user).data,
        "friends": UserSerializer(all_friends, many=True).data,
        "requests": FriendRequestSerializer(requests, many=True).data,
    }, safe=False)


@api_view(['POST'])
def send_friend_request(request, pk):
    user = User.objects.get(pk=pk)
    print(user, request.user)
    request_flag_user = FriendRequest.objects.filter(
        created_for=request.user).filter(created_by=user)
    request_flag_request_user = FriendRequest.objects.filter(
        created_for=user).filter(created_by=request.user)
    print(request_flag_user or request_flag_request_user)
    if not (request_flag_user or request_flag_request_user):
        FriendRequest.objects.create(created_for=user, created_by=request.user)
        return JsonResponse({"msg": "Friend request sent!"})
    return JsonResponse({"msg": "Friend request already sent!"})


@api_view(['POST'])
def handle_friend_request(request, pk, status):
    user = User.objects.get(pk=pk)
    friend_request = FriendRequest.objects.filter(
        created_for=request.user).get(created_by=user)
    if status == FriendRequestStatus.ACCEPTED.name:
        friend_request.status = FriendRequestStatus.ACCEPTED.value
    else:
        friend_request.status = FriendRequestStatus.REJECTED.value
    friend_request.save()
    user.friends.add(request.user)
    user.friends_count += 1
    user.save()
    request_user = request.user
    request_user.friends_count += 1
    request_user.save()
    return JsonResponse({"msg": f"Friend Request {status}"})
