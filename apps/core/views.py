from django.contrib.sites.models import Site
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_json_api.parsers import JSONParser as JSONAPIParser
from rest_framework_json_api.renderers import JSONRenderer as JSONAPIRenderer

from .serializers import SiteSerializer


class SiteViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Site.objects.get_queryset().order_by("id")
    allowed_methods = ["GET", "OPTIONS"]
    serializer_class = SiteSerializer
    # pylint: disable=duplicate-code
    parser_classes = (
        JSONAPIParser,
        MultiPartParser,
        FormParser,
    )  # pylint: disable=duplicate-code
    renderer_classes = (
        JSONAPIRenderer,
        BrowsableAPIRenderer,
    )  # pylint: disable=duplicate-code


def index(request):
    return render(request, "index.html")
