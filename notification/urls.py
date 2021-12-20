from django.urls import path, include

from .views import GetNotiByUserSerializer, UpdateReadNotificationView

urlpatterns = [
    path('api/notifications', GetNotiByUserSerializer.as_view(), name='list_noti'),
    path('api/categories/<int:pk>', UpdateReadNotificationView.as_view(), name='update_read'),
]