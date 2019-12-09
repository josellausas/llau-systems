from django.urls import path
from django.conf.urls import url, include
from . import views
from . import serializers

from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', serializers.UserViewSet)
router.register(r'groups', serializers.GroupViewSet)
router.register(r'apps', serializers.AppViewSet)

urlpatterns = [
    # path('', views.api_home, name='index'),
    url('', include(router.urls)),
    path('test/', views.api_test, name='test'),
]
