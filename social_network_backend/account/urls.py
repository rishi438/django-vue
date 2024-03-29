from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path("user_details/", api.user_details, name="user_details"),
    path("signup/", api.signup, name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("friends/<uuid:pk>/", api.friends, name="friends"),
    path(
        "friends/<uuid:pk>/request/",
        api.send_friend_request,
        name="send_friend_request",
    ),
    path(
        "friends/<uuid:pk>/<str:status>/",
        api.handle_friend_request,
        name="handle_friend_request",
    ),
    path(
        "profile/<uuid:pk>/edit/", api.user_details_update, name="user_details_update"
    ),
]
