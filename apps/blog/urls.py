from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home),
    path('<str:slug>/', views.blog_post_detail),
    path('<str:slug>/edit/', views.blog_post_create),
    path('<str:slug>/remove/', views.blog_post_remove),
]
