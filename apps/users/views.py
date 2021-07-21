from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth import get_user_model
from rest_framework import generics, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework_json_api.parsers import JSONParser as JSONAPIParser
from rest_framework_json_api.renderers import JSONRenderer as JSONAPIRenderer

from .filters import UserFilter
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer

UserModel = get_user_model()


class UserListView(viewsets.ModelViewSet):
    queryset = UserModel.objects.get_queryset().order_by("id")
    serializer_class = UserSerializer
    allowed_methods = ["GET", "OPTIONS", "PATCH"]
    filterset_class = UserFilter
    parser_classes = (
        JSONAPIParser,
        MultiPartParser,
        FormParser,
    )
    renderer_classes = (
        JSONAPIRenderer,
        BrowsableAPIRenderer,
    )
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "https://localhost:4200/oauth2callback"


class CurrentUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    allowed_methods = ["GET", "OPTIONS"]
    permission_classes = (IsAuthenticated,)
    renderer_classes = (
        JSONAPIRenderer,
        BrowsableAPIRenderer,
    )

    def get(self, request):
        return Response(
            self.get_serializer(request.user).data, status=status.HTTP_200_OK
        )
