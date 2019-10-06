"""llausys URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from apps.blog.views import blog_post_create
from apps.accounts.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', login_view),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('blog-new/', blog_post_create),
    re_path(r'^services?/$', views.services),
    path('about/', views.services),
    re_path(r'^projects?/$', views.projects),
    path('tech/', views.techs),
    path('contact/', views.contact),
]
