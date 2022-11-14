from rest_framework import generics, viewsets
from apps.todos.serializers import ToDoSerializer
from apps.todos.models import ToDo

# Create your views here.
# CRUD Operations


class ToDoListView(viewsets.ModelViewSet):  # Read # pylint: disable=too-many-ancestors
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetailView(generics.RetrieveUpdateAPIView):  # Update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoCreateView(generics.CreateAPIView):  # Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDeleteView(generics.DestroyAPIView):  # Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
