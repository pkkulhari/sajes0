from django.urls import path

from core.views import (
    HomeView,
    AboutView,
    GalleryListView,
    GalleryMediaView,
    GalleryImageView,
    GalleryVideoView,
    EventListView,
    EventDetailView,
    NewsListView,
    NewsDetailView,
    ContactView,
)

app_name = "core"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("gallery/", GalleryListView.as_view(), name="gallery"),
    path(
        "gallery-album/<int:pk>/media/",
        GalleryMediaView.as_view(),
        name="gallery-media",
    ),
    path(
        "gallery-album/<int:pk>/images/",
        GalleryImageView.as_view(),
        name="gallery-images",
    ),
    path(
        "gallery-album/<int:pk>/videos/",
        GalleryVideoView.as_view(),
        name="gallery-videos",
    ),
    path("events/", EventListView.as_view(), name="events"),
    path("events/<slug:slug>/", EventDetailView.as_view(), name="event-detail"),
    path("news/", NewsListView.as_view(), name="news"),
    path("news/<slug:slug>/", NewsDetailView.as_view(), name="news-detail"),
    path("contact/", ContactView.as_view(), name="contact"),
]
