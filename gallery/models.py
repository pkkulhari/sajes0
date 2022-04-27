from django.db import models

INSTITUTE_CHOICES = [
    ("SC", "Shrinathji College"),
    ("SS", "Shrinathji School"),
]


class GalleryAlbum(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateField()
    thumbnail = models.ImageField(upload_to="gallery/")
    institute = models.CharField(max_length=5, choices=INSTITUTE_CHOICES)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    album = models.ForeignKey(
        GalleryAlbum, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="gallery/albums/")
    uuid = models.UUIDField()
    thumbnail = models.ImageField(upload_to="gallery/albums/thumbnail")


class GalleryVideo(models.Model):
    album = models.ForeignKey(
        GalleryAlbum, on_delete=models.CASCADE, related_name="videos"
    )
    url = models.CharField(max_length=255)
