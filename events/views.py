from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from events.models import Event
from events.forms import EventForm


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = "events"
    extra_context = {"title": "Events"}


class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = "events/event_form.html"
    form_class = EventForm
    success_url = reverse_lazy("dashboard:events:event-list")
    extra_context = {"title": "Add Event"}


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = "events/event_form.html"
    form_class = EventForm
    success_url = reverse_lazy("dashboard:events:event-list")
    extra_context = {"title": "Update Event"}


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy("dashboard:events:event-list")
