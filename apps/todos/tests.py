from django.test import TestCase


from apps.todos.models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo")
        Todo.objects.create(
            title="second todo",
            is_completed=True,
        )

    def test_content_title(self):
        todo = Todo.objects.get(id=1)
        expected_title = f"{todo.title}"
        self.assertEqual(expected_title, "first todo")

    def test_content_is_completed(self):
        todo = Todo.objects.get(id=2)
        expected_is_completed = f"{todo.is_completed}"
        self.assertEqual(expected_is_completed, "True")
