from django import forms
from .models import *
from account.models import Account
from track.models import Track

class CreateTraineeModel(forms.ModelForm):
    account_obj = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        required=False,
        label="Account",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    track_obj = forms.ModelChoiceField(
        queryset=Track.objects.all(),
        required=False,
        label="Track",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Trainee
        fields = [
            "first_name",
            "last_name",
            "age",
            "photo",
            "account_obj",
            "track_obj",
        ]

class UpdateTrainee(forms.Form):
    first_name = forms.CharField(
        required=True,
        max_length=20,
        label="First Name",
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
    )

    last_name = forms.CharField(
        required=True,
        max_length=20,
        label="Last Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
    )

    age = forms.DateField(
        required=True,
        label="Age",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    photo = forms.ImageField(
        required=False,
        label="Photo",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "photo/*"}
        ),
    )
    account_obj = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        required=True,
        label="Account",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    track_obj = forms.ModelChoiceField(
        queryset=Track.objects.all(),
        required=True,
        label="Track",
        widget=forms.Select(attrs={"class": "form-control"}),
    )