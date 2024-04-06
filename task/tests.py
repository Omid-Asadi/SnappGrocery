from django.test import TestCase
from .models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="t-01", body='b-01')

    def test_title(self):
        self.assertTrue(isinstance(self.task.title, str))

    def test_body(self):
        self.assertTrue(isinstance(self.task.body, str))
