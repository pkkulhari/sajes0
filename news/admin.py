from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news.models import News


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(News, NewsAdmin)
