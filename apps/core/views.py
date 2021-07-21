from django.contrib.sites.models import Site
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_json_api.parsers import JSONParser as JSONAPIParser
from rest_framework_json_api.renderers import JSONRenderer as JSONAPIRenderer

from .serializers import SiteSerializer


class SiteListView(viewsets.ModelViewSet):
    queryset = Site.objects.get_queryset().order_by("id")
    allowed_methods = ["GET", "OPTIONS"]
    serializer_class = SiteSerializer
    parser_classes = (
        JSONAPIParser,
        MultiPartParser,
        FormParser,
    )
    renderer_classes = (
        JSONAPIRenderer,
        BrowsableAPIRenderer,
    )


def index(request):
    return render(request, "core/index.html")
