from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.text import slugify
from django.db import models
from io import BytesIO
from PIL import Image
import sys

INSTITUTE_CHOICES = [
    ("SC", "Shrinathji College"),
    ("SS", "Shrinathji School"),
]


class Event(models.Model):
    title = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    finish_datetime = models.DateTimeField()
    address = models.TextField()
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    thumbnail = models.ImageField(upload_to="events/")
    institute = models.CharField(max_length=5, choices=INSTITUTE_CHOICES)

    def save(self):
        # Slug
        self.slug = self.slug or slugify(self.title)

        super(Event, self).save()

    def __str__(self):
        return self.title
