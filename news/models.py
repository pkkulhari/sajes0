from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.text import slugify
from django.db import models
from PIL import Image
from io import BytesIO
import sys

INSTITUTE_CHOICES = [
    ("SC", "Shrinathji College"),
    ("SS", "Shrinathji School"),
]


class News(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateField()
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    thumbnail = models.ImageField(upload_to="news/")
    institute = models.CharField(max_length=5, choices=INSTITUTE_CHOICES)

    def save(self):
        # Slug
        self.slug = self.slug or slugify(self.title)

        super(News, self).save()

    def get_content_preview(self):
        return self.content[:250]

    def __str__(self):
        return self.title
