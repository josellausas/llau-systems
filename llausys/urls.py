"""llausys URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from apps.blog.views import blog_post_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('blog-new/', blog_post_create),
    # TODO:
    re_path(r'^services?/$', views.services),
    path('about/', views.services),
    re_path(r'^projects?/$', views.projects),
    path('tech/', views.techs),
    path('contact/', views.contact),
]
