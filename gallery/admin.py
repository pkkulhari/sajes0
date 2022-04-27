from django.contrib import admin

from gallery.models import GalleryAlbum, GalleryImage, GalleryVideo

admin.site.register(GalleryAlbum)
admin.site.register(GalleryImage)
admin.site.register(GalleryVideo)
