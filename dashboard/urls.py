from django.urls import path, include

from dashboard.views import HomeView
from events import urls as event_urls
from news import urls as news_urls
from gallery import urls as gallery_urls

app_name = "dashboard"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("events/", include(event_urls, namespace="events")),
    path("news/", include(news_urls, namespace="news")),
    path("gallery/", include(gallery_urls, namespace="gallery")),
]
