from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserModelChangeForm, UserModelCreationForm
from .models import User


class UserModelAdmin(UserAdmin):
    add_form = UserModelCreationForm
    form = UserModelChangeForm
    model = User
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "language",
        "dark_mode",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "last_login",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        (
            "Custom Profile",
            {
                "fields": (
                    "language",
                    "dark_mode",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Timestamps", {"classes": ("collapse",), "fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserModelAdmin)
