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

from cart.views import ListCreateCartAPIView, UpdateDeleteCartView, ActiveCartAPIView, ListCreateCartItemsAPIView, UpdateDeleteCartItemsView, GetAllItemsInCartAPIView

urlpatterns = [
    path('api/carts', ListCreateCartAPIView.as_view(), name='list_create'),
    path('api/carts/update/<int:pk>', UpdateDeleteCartView.as_view(), name='update'),
    path('api/carts/delete/<int:pk>', UpdateDeleteCartView.as_view(), name='delete'),
    path('api/carts/cart_active', ActiveCartAPIView.as_view()),

    path('api/cart_items', ListCreateCartItemsAPIView.as_view(), name="list_create_ci"),
    path('api/cart_items/<int:pk>', UpdateDeleteCartItemsView.as_view()),
    path('api/cart_items/cart/<int:cart_id>', GetAllItemsInCartAPIView.as_view()),
]