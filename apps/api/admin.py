from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.MobileApp)
admin.site.register(models.Score)
admin.site.register(models.UserGame)
