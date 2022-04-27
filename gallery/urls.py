from django.urls import path

from gallery.views import (
    AlbumListView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
    MediaListView,
    MediaDeleteView,
    MediaCreateView,
)

app_name = "gallery"
urlpatterns = [
    path("albums/", AlbumListView.as_view(), name="album-list"),
    path("albums/add/", AlbumCreateView.as_view(), name="album-create"),
    path(
        "albums/<int:pk>/update/",
        AlbumUpdateView.as_view(),
        name="album-update",
    ),
    path(
        "albums/<int:pk>/delete/",
        AlbumDeleteView.as_view(),
        name="album-delete",
    ),
    path(
        "albums/<int:pk>/media/",
        MediaListView.as_view(),
        name="media-list",
    ),
    path(
        "albums/<int:pk>/media/delete/",
        MediaDeleteView.as_view(),
        name="media-delete",
    ),
    path(
        "albums/<int:pk>/media/create/",
        MediaCreateView.as_view(),
        name="media-create",
    ),
]
