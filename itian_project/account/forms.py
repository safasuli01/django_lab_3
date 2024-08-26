from django import forms

class CreateAccount(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=50,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        required=True,
        max_length=200,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
    )


class UpdateAccount(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        required=False,
        max_length=200,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
    )