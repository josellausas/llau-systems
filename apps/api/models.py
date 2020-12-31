from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class MobileApp(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("api:app-detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['slug']
    

class UserGame(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time_played = models.IntegerField(default=0)
    game = models.ForeignKey(MobileApp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_owned = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.game}:{self.user}"

    class Meta:
        ordering = ['created']


class Score(models.Model):
    score = models.IntegerField(blank=False, default=0, null=False)
    app = models.ForeignKey(MobileApp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.app}){self.user}: {self.score}"
    
    class Meta:
        ordering = ['created']
