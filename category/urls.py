from django.urls import path, include

from .views import ListCreateCategoryAPIView, UpdateDeleteCategoryView

urlpatterns = [
    path('api/categories', ListCreateCategoryAPIView.as_view(), name='list_create'),
    path('api/categories/<int:pk>', UpdateDeleteCategoryView.as_view(), name='update_delete'),
]