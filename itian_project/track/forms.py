from django import forms
from .models import *

class CreateTrack(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=30,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Description", "class": "form-control"}
        ),
    )
    description = forms.CharField(
        required=True,
        label="Description",
        widget=forms.Textarea(
            attrs={"placeholder": "Description", "class": "form-control"}
        ),
    )
    photo = forms.ImageField(required=False, label="photo", widget=forms.FileInput())

class CreateTrackModel(forms.ModelForm):
    class Meta:
        model = Track
        fields = "__all__"


class UpdateTrack(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=30,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Name", "class": "form-control"}
        ),
    )
    description = forms.CharField(
        required=True,
        label="Description",
        widget=forms.Textarea(
            attrs={"placeholder": "Description", "class": "form-control"}
        ),
    )
    photo = forms.ImageField(
        required=False,
        label="photo",
        widget=forms.FileInput(),
    )