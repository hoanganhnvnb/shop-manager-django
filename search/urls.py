from django.urls import path, include

from search.views import GetItemsByTitle, GetItemsByCompanyName, GetItemsByCategoryTitle

urlpatterns = [
    path('api/item/<slug:search_text>', GetItemsByTitle.as_view()),
    path('api/company/<slug:search_text>', GetItemsByCompanyName.as_view()),
    path('api/category/<slug:search_text>', GetItemsByCategoryTitle.as_view()),
]