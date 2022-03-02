from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from gallery.models import GalleryAlbum, GalleryImage, GalleryVideo
from gallery.forms import GalleryAlbumForm


class AlbumListView(LoginRequiredMixin, ListView):
    model = GalleryAlbum
    template_name = "gallery/album/album_list.html"
    context_object_name = "albums"
    extra_context = {"title": "Albums | Gallery"}


class AlbumCreateView(LoginRequiredMixin, CreateView):
    template_name = "gallery/album/album_form.html"
    form_class = GalleryAlbumForm
    success_url = reverse_lazy("dashboard:gallery:album-list")
    extra_context = {"title": "Add Album | Gallery"}


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = GalleryAlbum
    template_name = "gallery/album/album_form.html"
    form_class = GalleryAlbumForm
    success_url = reverse_lazy("dashboard:gallery:album-list")
    extra_context = {"title": "Update Album | Gallery"}


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = GalleryAlbum
    success_url = reverse_lazy("dashboard:gallery:album-list")


class MediaListView(LoginRequiredMixin, View):
    def get(self, request, pk):
        images = GalleryImage.objects.filter(album=pk)

        videos = GalleryVideo.objects.filter(album=pk)
        context = {
            "title": "Media | Album",
            "albumId": pk,
            "images": images,
            "videos": videos,
        }

        return render(request, "gallery/media/media_form.html", context=context)


class MediaDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        vid = request.POST.get("vid")
        imageUUID = request.POST.get("imageUUID")

        album = GalleryAlbum.objects.get(id=pk)

        if vid:
            GalleryVideo.objects.get(album=album, url=vid).delete()
            return HttpResponse(status=204)
        elif imageUUID:
            GalleryImage.objects.get(uuid=imageUUID, album=album).delete()
            return HttpResponse(status=204)

        return HttpResponse(status=422)


class MediaCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        vid = request.POST.get("vid")

        album = GalleryAlbum.objects.get(id=pk)

        if len(request.FILES):
            image = request.FILES["image"]
            imageUUID = request.POST.get("imageUUID")

            image.name = imageUUID + "." + image.content_type.split("/")[1]
            GalleryImage.objects.create(album=album, image=image, uuid=imageUUID)

            return HttpResponse(status=204)

        elif vid:
            GalleryVideo.objects.create(album=album, url=vid)
            return HttpResponse(status=204)

        return HttpResponse(status=422)
