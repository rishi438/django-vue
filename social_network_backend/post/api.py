from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

# Create your views here.


@api_view(["GET"])
def post_list():
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)
