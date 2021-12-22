from django.urls import path, include

from .views import GetNotiByUserSerializer, UpdateReadNotificationView, UpdateDeleteNotificationView

urlpatterns = [
    path('api/notifications', GetNotiByUserSerializer.as_view(), name='list_noti'),
    path('api/notifications/<int:pk>', UpdateReadNotificationView.as_view(), name='update_read'),
    path("api/notifications/delete/<int:pk>", UpdateDeleteNotificationView.as_view(), name="delete")
]