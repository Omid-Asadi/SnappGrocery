from rest_framework import serializers
from lib.database.in_memory_db.database import TaskInMemoryDatabase
from task.models import Task


class TaskDBSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Task


class TaskInMemorySerializer:
    @classmethod
    def get_list_data(cls):
        return TaskInMemoryDatabase().repository
