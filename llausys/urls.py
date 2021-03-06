"""llausys URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from apps.blog.views import blog_post_create
from apps.accounts.views import (
    login_view, logout_view, signup_view, my_profile_view
)

# Admin panel config
admin.site.site_header = "Llau Systems"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Welcome to Llau Systems Admin"

urlpatterns = [
    path('api-token/', obtain_auth_token, name="api_token"),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', my_profile_view, name='profile'),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('blog-new/', blog_post_create),
    re_path(r'^services?/$', views.services),
    path('about/', views.services),
    re_path(r'^projects?/$', views.projects),
    path('tech/', views.techs),
    path('contact/', views.contact),
    path('api/v1/', include('apps.api.urls', namespace='api')),
    path('thanks/', views.notify_confirm, name="thanks"),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
