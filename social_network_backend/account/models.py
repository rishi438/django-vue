import uuid
from enum import IntEnum, unique
from typing import Any
from uuid import uuid4

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# from django.contrib.admin.forms import AdminPasswordChangeForm
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(
        self, name: str, email: str | None, password: str | None, **extra_fields: Any
    ) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        user = self.create_user(
            email=email, password=password, name=name, **extra_fields
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=225, unique=True, default="")
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    friends = models.ManyToManyField("self")
    friends_count = models.IntegerField(default=0)
    posts_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    objects = CustomUserManager()


# class UserPasswordUpdate(AdminPasswordChangeForm):
#     def save(self, commit: bool = True) -> AbstractBaseUser:
#         password = self.cleaned_data["password1"]
#         self.user.set_password(password)
#         return super().save(commit)


@unique
class FriendRequestStatus(IntEnum):
    SENT = 0
    ACCEPTED = 1
    REJECTED = 2


class FriendRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(
        User, related_name="recieved_friend_request", on_delete=models.CASCADE
    )
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_friend_request", on_delete=models.CASCADE
    )
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in FriendRequestStatus],
        default=FriendRequestStatus.SENT.value,
    )
    rejection_count = models.IntegerField(default=0, validators=[MaxValueValidator(3)])
