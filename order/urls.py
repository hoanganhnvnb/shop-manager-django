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

from order.views import ListCreateOrderAPIView, UpdateDeleteOrderView, UpdateTotalOrderAPIView, OrderPaidAPIView, GetOrderCompleteByUser, GetOrderById

urlpatterns = [
    path('api/orders', ListCreateOrderAPIView.as_view(), name='list_create'),
    path('api/orders/<int:pk>', UpdateDeleteOrderView.as_view(), name='update_delete'),
    path('api/orders/update_total/<int:pk>', UpdateTotalOrderAPIView.as_view(), name='total'),
    path('api/orders/paid/<int:pk>', OrderPaidAPIView.as_view(), name='paid'),
    path('api/orders/his_order', GetOrderCompleteByUser.as_view()),
    path('api/orders/order/<int:pk>', GetOrderById.as_view())
]