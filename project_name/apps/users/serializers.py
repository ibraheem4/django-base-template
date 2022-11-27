from django.contrib.auth import get_user_model
from rest_framework_json_api import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):  # pylint: disable=too-many-ancestors
    class Meta:
        model = UserModel
        fields = (
            "email",
            "language",
            "username",
            "first_name",
            "last_name",
            "dark_mode",
        )
