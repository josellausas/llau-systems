from django.conf.urls import url, include
from django.contrib.auth import get_user_model, models

from rest_framework import routers, serializers, viewsets

from .models import MobileApp, Score

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:group-detail")
    class Meta:
        model = models.Group
        fields = ['url', 'name']

class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = GroupSerializer

class AppSerializer(serializers.Serializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:app-detail", lookup_field='slug')
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MobileApp.objects.all()
    serializer_class = AppSerializer
