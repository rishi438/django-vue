from account.models import User
from account.serializers import UserSerializer
from django.http import JsonResponse
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from utils.constant import API_RESPONSE_OBJ, RESPONSE_MSG_API, RESPONSE_STATUS_API


@api_view(["POST"])
def search(request):
    """This function searches all posts and all users

    Args:
        request (object): contains request details

    Returns:
        response(dict): status of operation and conversation detail
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        data = request.data
        query = data["query"]
        users = User.objects.filter(name__icontains=query)
        posts = Post.objects.filter(body__icontains=query)
        if users or posts:
            response["users"] = UserSerializer(users, many=True).data
            response["posts"] = PostSerializer(posts, many=True).data
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "list of user or posts fetched."
    except Exception as ex:
        print(f"Error api_view.search: {ex}")
    return JsonResponse(response, safe=False)
