from django.test import TestCase

# Create your tests here.
from apps.todos.models import ToDo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ToDo.objects.create(
            title="first todo", description="a description here", date="2022-11-13"
        )
        ToDo.objects.create(
            title="second todo",
            description="a description here",
            date="2022-11-13",
            completed=True,
        )

    def test_content_title(self):
        todo = ToDo.objects.get(id=1)
        expected_title = f"{todo.title}"
        self.assertEqual(expected_title, "first todo")

    def test_content_description(self):
        todo = ToDo.objects.get(id=1)
        expected_description = f"{todo.description}"
        self.assertEqual(expected_description, "a description here")

    def test_content_date(self):
        todo = ToDo.objects.get(id=1)
        expected_date = f"{todo.date}"
        self.assertEqual(expected_date, "2022-11-13")

    def test_content_completed(self):
        todo = ToDo.objects.get(id=2)
        expected_completed = f"{todo.completed}"
        self.assertEqual(expected_completed, "True")
