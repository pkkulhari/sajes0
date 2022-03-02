from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from events.models import Event


class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(Event, EventAdmin)
