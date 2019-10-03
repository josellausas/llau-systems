from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)
