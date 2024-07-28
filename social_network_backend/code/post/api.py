from code.account.models import User
from code.account.serializers import UserSerializer
from code.utils.constant import API_RESPONSE_OBJ, RESPONSE_MSG_API, RESPONSE_STATUS_API
from collections import defaultdict

from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .forms import PostForm
from .models import Comment, Like, Post, Trends
from .serializers import (
    CommentSerializer,
    PostDetailSerializer,
    PostSerializer,
    TrendsSerializer,
)


@api_view(["GET"])
def post_list(request):
    """This function fetches list of post's

    Args:
        request (object): contains request details

    Returns:
        response(dict): status of operation and list of post's
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        user_ids = [request.user.id]
        for user in request.user.friends.all():
            user_ids.append(user.id)
        posts = Post.objects.filter(created_by__in=user_ids)

        if posts:
            trend = request.GET.get("trend", None)
            if trend:
                posts = posts.filter(body__icontains="#" + trend)
            response["payload"] = PostSerializer(posts, many=True).data
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "list of posts fetched."
    except Exception as ex:
        print(f"Error api_view.post_list: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["GET"])
def post_list_profile(request, pk):
    """This function fetches list of posts

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        response(dict): status of operation and list of posts details
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        user = User.objects.get(pk=pk)
        posts = Post.objects.filter(created_by_id=pk)
        print(posts, user)
        if user or posts:
            response["payload"] = {}
            response["payload"]["posts"] = PostSerializer(posts, many=True).data
            response["payload"]["user"] = UserSerializer(user).data
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "Lists posts of a user fetched."
    except Exception as ex:
        print(f"Error api_view.post_list_profile: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["POST"])
def post_create(request):
    """ "This function creates post

    Args:
        request (object): contains request details

    Returns:
        response(dict): status of operation and post details
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        form = PostForm(request.data)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            user = User.objects.get(pk=request.user.id)
            user.posts_count += 1
            user.save()
            post.save()
            response["payload"] = PostSerializer(post).data
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "Post created successfully."
    except Exception as ex:
        print(f"Error api_view.post_create: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["POST"])
def post_like(request, pk):
    """This function adds like to the post or comment

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        response(dict): status of operation
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        post = Post.objects.get(pk=pk)
        if not post.likes.filter(created_by=request.user):
            like = Like.objects.create(created_by=request.user)
            post.likes_count += 1
            post.likes.add(like)
            post.save()
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "Post liked successfully."
        else:
            response[RESPONSE_MSG_API] = "Post already liked."
    except Exception as ex:
        print(f"Error api_view.post_like: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["GET"])
def post_detail(request, pk):
    """This function fetches post details

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        response(dict): status of operation and post details
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        post = Post.objects.get(pk=pk)
        if post:
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "post detail fetched."
            response["payload"] = {}
            response["payload"]["post"] = PostDetailSerializer(post).data
    except Exception as ex:
        print(f"Error api_view.post_detail: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["POST"])
def post_create_comment(request, pk):
    """This function creates comments for a post

    Args:
        request (object): contains request details
        pk (uuid): unique id of the specific user

    Returns:
        response(dict): status of operation and post comment details
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        comment = Comment.objects.create(
            body=request.data.get("body"), created_by=request.user
        )
        post = Post.objects.get(pk=pk)
        if comment and post:
            response["payload"] = CommentSerializer(comment).data
            if response["payload"]:
                post.comments.add(comment)
                post.comments_count += 1
                post.save()
                response[RESPONSE_STATUS_API] = True
                response[RESPONSE_MSG_API] = "post comment created."
    except Exception as ex:
        print(f"Error api_view.post_create_comment: {ex}")
    return JsonResponse(response, safe=False)


@api_view(["GET"])
def get_trends(request):
    """This function fetches top trends in 24hrs

    Returns:
        request (object): contains request details and trends details
    """
    response = API_RESPONSE_OBJ.copy()
    response[RESPONSE_MSG_API] = "Error Occured. Please Try again later."
    try:
        response["payload"] = TrendsSerializer(Trends.objects.all(), many=True).data
        if response["payload"]:
            response[RESPONSE_STATUS_API] = True
            response[RESPONSE_MSG_API] = "Fetched Trends in 24 hrs."
    except Exception as ex:
        print(f"Error api_view.get_trends: {ex}")
    return JsonResponse(response, safe=False)
