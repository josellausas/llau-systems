from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.api_home, name='index'),
    path('test/', views.api_test, name='test'),
]
