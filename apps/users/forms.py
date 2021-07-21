from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserModelCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("email",)


class UserModelChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
