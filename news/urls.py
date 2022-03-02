from django.urls import path

from news.views import (
    NewsListView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
)

app_name = "news"
urlpatterns = [
    path("", NewsListView.as_view(), name="news-list"),
    path("add/", NewsCreateView.as_view(), name="news-create"),
    path("<int:pk>/update/", NewsUpdateView.as_view(), name="news-update"),
    path("<int:pk>/delete/", NewsDeleteView.as_view(), name="news-delete"),
]
