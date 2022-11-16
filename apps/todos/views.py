from rest_framework import viewsets
from apps.todos.serializers import TodoSerializer
from apps.todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
