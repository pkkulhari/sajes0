from django import forms
from django.forms.fields import DateField
from django.forms.widgets import DateInput
from django_summernote.widgets import SummernoteWidget

from news.models import News


class NewsForm(forms.ModelForm):

    created = DateField(
        input_formats=["%Y-%m-%d"],
        widget=DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = News
        fields = "__all__"
        exclude = ("slug",)
        widgets = {
            "content": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
