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

    def clean_avatar(self):
        avatar = self.cleaned_data["avatar"]
        return avatar

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["avatar"]:
            user.avatar = self.cleaned_data["avatar"]
        if commit:
            user.save()
        return user
