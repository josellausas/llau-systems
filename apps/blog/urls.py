from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='index'),
    path('<str:slug>/', views.blog_post_detail, name='detail'),
    path('<str:slug>/edit/', views.blog_post_update, name='edit'),
    path('<str:slug>/remove/', views.blog_post_remove, name='remove'),
]
