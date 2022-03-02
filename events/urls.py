from django.urls import path

from events.views import (
    EventListView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

app_name = "events"
urlpatterns = [
    path("", EventListView.as_view(), name="event-list"),
    path("add/", EventCreateView.as_view(), name="event-create"),
    path("<int:pk>/update/", EventUpdateView.as_view(), name="event-update"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event-delete"),
]
