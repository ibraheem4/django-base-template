from rest_framework_json_api import serializers
from project_name.apps.todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):  # pylint: disable=too-many-ancestors
    class Meta:
        model = Todo
        fields = ("id", "title", "is_completed")
