from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    language = models.CharField(max_length=16, null=True, blank=True)
    dark_mode = models.BooleanField(
        _("dark mode"),
        null=False,
        default=False,
        help_text="Enable Dark Mode for this user",
    )
    username = models.CharField(max_length=64, null=True, blank=True, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class JSONAPIMeta:
        resource_name = "users"
        JSON_API_PLURALIZE_TYPES = True

    def __str__(self):
        return self.email
