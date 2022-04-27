from django import forms
from django.forms.fields import DateTimeField
from django.forms.widgets import DateTimeInput
from django_summernote.widgets import SummernoteWidget

from events.models import Event


class EventForm(forms.ModelForm):

    start_datetime = DateTimeField(
        input_formats=["%d-%m-%Y %I:%M %p"],
        widget=DateTimeInput(format="%d-%m-%Y %I:%M %p"),
    )
    finish_datetime = DateTimeField(
        input_formats=["%d-%m-%Y %I:%M %p"],
        widget=DateTimeInput(format="%d-%m-%Y %I:%M %p"),
    )

    class Meta:
        model = Event
        fields = "__all__"
        exclude = ("slug",)
        widgets = {
            "content": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

        self.fields["start_datetime"].widget.attrs["class"] += " datetimepicker"
        self.fields["finish_datetime"].widget.attrs["class"] += " datetimepicker"
        self.fields["address"].widget.attrs["rows"] = 3
