from django import forms
from django.forms.fields import DateField
from django.forms.widgets import DateInput

from gallery.models import GalleryAlbum


class GalleryAlbumForm(forms.ModelForm):

    created = DateField(
        input_formats=["%Y-%m-%d"],
        widget=DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = GalleryAlbum
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GalleryAlbumForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
