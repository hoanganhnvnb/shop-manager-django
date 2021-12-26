from django.urls import path, include
from .views import GetReport


urlpatterns = [
    path('get', GetReport.as_view()),
]