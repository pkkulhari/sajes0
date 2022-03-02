from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from events.models import Event
from news.models import News
from gallery.models import GalleryAlbum, GalleryImage, GalleryVideo


class HomeView(View):
    def get(self, request):
        events = Event.objects.all().order_by("-id")[:3]
        news_objs = News.objects.all().order_by("-id")[:3]
        context = {
            "title": "SAJES - Shree Amar Jyoti Education Society",
            "events": events,
            "news_objs": news_objs,
        }

        return render(request, "core/home.html", context)


class AboutView(View):
    def get(self, request):
        context = {"title": "About | SAJES"}

        return render(request, "core/about.html", context)


class GalleryListView(ListView):
    model = GalleryAlbum
    template_name = "core/gallery.html"
    context_object_name = "albums"
    extra_context = {"title": "Gallery | SAJES"}
    ordering = ["-created"]
    paginate_by = 9


class GalleryMediaView(View):
    def get(self, request, pk):
        page_number = request.GET.get("page")

        images = GalleryImage.objects.filter(album=pk).order_by("-id")
        videos = []

        if page_number is None or int(page_number) == 1:
            videos = GalleryVideo.objects.filter(album=pk).order_by("-id")

        paginator = Paginator(images, 12)
        page_obj = paginator.get_page(page_number)

        context = {
            "title": "Gallery Media | SAJES",
            "videos": videos,
            "page_obj": page_obj,
            "pk": pk,
        }

        return render(request, "core/gallery-media.html", context)


class GalleryImageView(View):
    def get(self, request, pk):
        images = GalleryImage.objects.filter(album=pk).order_by("-id")

        page_number = request.GET.get("page")
        paginator_img = Paginator(images, 12)
        page_obj = paginator_img.get_page(page_number)

        context = {
            "title": "Gallery Images | SAJES",
            "page_obj": page_obj,
            "pk": pk,
        }

        return render(request, "core/gallery-media.html", context)


class GalleryVideoView(View):
    def get(self, request, pk):
        videos = GalleryVideo.objects.filter(album=pk).order_by("-id")

        context = {
            "title": "Gallery Videos | SAJES",
            "videos": videos,
            "pk": pk,
        }

        return render(request, "core/gallery-media.html", context)


class EventListView(ListView):
    template_name = "core/events.html"
    context_object_name = "events"
    extra_context = {"title": "Events | SAJES"}
    paginate_by = 5

    def get_queryset(self):
        events = None
        filter = self.request.GET.get("filter", "upcomming")

        if filter == "happening":
            events = Event.objects.filter(
                start_datetime__lte=timezone.now(), finish_datetime__gte=timezone.now()
            ).order_by("-id")
        elif filter == "expired":
            events = Event.objects.filter(finish_datetime__lt=timezone.now()).order_by(
                "-id"
            )
        elif filter == "upcomming":
            events = Event.objects.filter(start_datetime__gt=timezone.now()).order_by(
                "-id"
            )

        return events


class EventDetailView(DetailView):
    model = Event
    template_name = "core/event-detail.html"
    context_object_name = "event"
    extra_context = {"title": "Event Detail | SAJES"}


class NewsListView(ListView):
    model = News
    template_name = "core/news.html"
    context_object_name = "news_obj"
    extra_context = {"title": "News | SAJES"}
    paginate_by = 5


class NewsDetailView(DetailView):
    model = News
    template_name = "core/news-detail.html"
    context_object_name = "news"
    extra_context = {"title": "News Detail | SAJES"}


class ContactView(View):
    def get(self, request):
        context = {"title": "Contact Us | SAJES"}

        return render(request, "core/contact.html", context)

    def post(self, request):
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")

        body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        if email and subject and message:
            send_mail(
                "Contact Form - SAJES",
                body,
                settings.EMAIL_HOST_USER,
                ["pkkulhari2020@gmail.com"],
                fail_silently=False,
            )
            return redirect("/contact/?status=success")

        return redirect("/contact/?status=error")
