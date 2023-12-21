import uuid

from account.models import User
from django.db import models


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="post_attachments")
    created_by = models.ForeignKey(
        User, related_name="post_attachments", on_delete=models.CASCADE)


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)

    # likes
    # likes_count

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)  # noqa

    def created_at_formatted(self):
        from django.utils.timesince import timesince
        return timesince(self.created_at)
