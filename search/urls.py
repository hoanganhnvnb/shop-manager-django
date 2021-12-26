from django.urls import path, include

from search.views import GetItemsByTitle, GetItemsByCompanyName, GetItemsByCategoryTitle

urlpatterns = [
    path('api/item', GetItemsByTitle.as_view()),
    path('api/company', GetItemsByCompanyName.as_view()),
    path('api/category', GetItemsByCategoryTitle.as_view()),
]