from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_json_api.parsers import JSONParser as JSONAPIParser
from rest_framework_json_api.renderers import JSONRenderer as JSONAPIRenderer
from project_name.apps.todos.serializers import TodoSerializer
from project_name.apps.todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    parser_classes = (
        JSONAPIParser,
        MultiPartParser,
        FormParser,
    )  # pylint: disable=duplicate-code
    renderer_classes = (
        JSONAPIRenderer,
        BrowsableAPIRenderer,
    )  # pylint: disable=duplicate-code
