from rest_framework_json_api import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'language', 'username', 'first_name', 'last_name', 'dark_mode')
