from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

UserModel = get_user_model()


class UserFilter(filters.FilterSet):
    class Meta:
        model = UserModel
        fields = {
            "email": ["exact"],
        }
