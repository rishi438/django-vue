from account.models import User
from account.serializers import UserSerializer
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
    user_ids = [request.user.id]
    for user in request.user.friends.all():
        user_ids.append(user.id)
    posts = Post.objects.filter(created_by__in=user_ids)
    trend = request.GET.get("trend", "")
    print(trend)
    if trend:
        posts = posts.filter(body__icontains="#" + trend)
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def post_list_profile(request, pk):
    user = User.objects.get(pk=pk)
    posts = Post.objects.filter(created_by_id=pk)
    post_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    return JsonResponse(
        {"post": post_serializer.data, "user": user_serializer.data}, safe=False
    )


@api_view(["POST"])
def post_create(request):
    form = PostForm(request.data)
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        user = User.objects.get(pk=request.user.id)
        user.posts_count += 1
        user.save()
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"error": "Error Occured contact Tech Team"})


@api_view(["POST"])
def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    if not post.likes.filter(created_by=request.user):
        like = Like.objects.create(created_by=request.user)
        post.likes_count += 1
        post.likes.add(like)
        post.save()
        return JsonResponse({"msg": "liked"})
    return JsonResponse({"msg": "already liked"})


@api_view(["GET"])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if post:
        return JsonResponse({"post": PostDetailSerializer(post).data}, safe=False)
    return JsonResponse({"msg": "Error Occured contact Tech Team"})


@api_view(["POST"])
def post_create_comment(request, pk):
    comment = Comment.objects.create(
        body=request.data.get("body"), created_by=request.user
    )
    post = Post.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count += 1
    post.save()
    serailizer = CommentSerializer(comment)
    if serailizer.data:
        return JsonResponse(serailizer.data, safe=False)
    return JsonResponse({"msg": "Error Occured contact Tech Team"})


@api_view(["GET"])
def get_trends(request):
    serializer = TrendsSerializer(Trends.objects.all(), many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)
