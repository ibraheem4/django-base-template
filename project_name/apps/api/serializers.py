from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


UserModel = get_user_model()


class MyTokenObtainPairSerializer(
    TokenObtainPairSerializer
):  # pylint: disable=abstract-method
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token["email"] = user.email
        # ...
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ("email", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = UserModel.objects.create(email=validated_data["email"])

        user.set_password(validated_data["password"])
        user.save()

        return user
