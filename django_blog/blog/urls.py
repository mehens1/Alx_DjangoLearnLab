# blog/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='blog/home.html'), name='home'),
    path('', include('blog.urls')),  # Include blog app URLs
]