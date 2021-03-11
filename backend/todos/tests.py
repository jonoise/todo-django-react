from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='test_todo', body='test_body__')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'test_todo')

    def test_body_content(self):
        todo = Todo.objects.get(pk=1)
        expected_object_body = f'{todo.body}'
        self.assertEquals(expected_object_body, 'test_body__')
