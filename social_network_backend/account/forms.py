from django.contrib.auth.forms import UserCreationForm, ValidationError
from django.forms import ModelForm

from .models import User


class SigupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")


class UserDetailsForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "avatar"]
