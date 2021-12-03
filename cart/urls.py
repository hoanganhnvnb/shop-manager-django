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

from cart.views import ListCreateCartAPIView, UpdateDeleteCartView

urlpatterns = [
    path('api/carts/<int:user_id>', ListCreateCartAPIView.as_view(), name='list_cart_user'),
    path('api/carts/create', ListCreateCartAPIView.as_view(), name='create_cart'),
    path('api/carts/update/<int:pk>', UpdateDeleteCartView.as_view(), name='update'),
    path('api/carts/delete/<int:pk>', UpdateDeleteCartView.as_view(), name='delete'),
]