from rest_framework_json_api import serializers
from apps.todos.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):  # pylint: disable=too-many-ancestors
  class Meta:
    model = ToDo
    fields = ("id", "title", "description", "date", "completed")