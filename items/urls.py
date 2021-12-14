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

from items.views import ListCreateItemsAPIView, UpdateDeleteItemsView, AddQuantityItemsView, AddImageItemsView, GetItemAPIView, ListPopularItemsAPIView

urlpatterns = [
    path('api/items', ListCreateItemsAPIView.as_view(), name='list_create'),
    path('api/items/<int:barcode>', UpdateDeleteItemsView.as_view(), name='update_delete'),
    path('api/items/add/<int:barcode>', AddQuantityItemsView.as_view(), name='add_quantity'),
    path('api/items/add_image/<int:barcode>', AddImageItemsView.as_view(), name='image'),
    path('api/items/get/<int:barcode>', GetItemAPIView.as_view(), name='get'),
    path('api/items/popular', ListPopularItemsAPIView.as_view, name='popular')
]