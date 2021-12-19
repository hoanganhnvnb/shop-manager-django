"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserRegisterAPIView, UserInformationAPIView, ListCreateUserAPIView, UpdateDeleteUserView, UpdateTokenUserView

urlpatterns = [
    path('api/login', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', UserRegisterAPIView.as_view(), name='register'),
    path('api/info', UserInformationAPIView.as_view(), name='info'),
    path('api/users', ListCreateUserAPIView.as_view(), name='create_list'),
    path('api/users/<int:pk>', UpdateDeleteUserView.as_view(), name='update_delete'),
    path('api/device_token', UpdateTokenUserView.as_view())
]