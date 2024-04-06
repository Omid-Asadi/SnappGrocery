import logging
from rest_framework import generics, status
from rest_framework.response import Response
from constants.database import IN_MEMORY, MAIN_DB
from task.api.v1.serializers import TaskDBSerializer, TaskInMemorySerializer
from task.models import Task
from django.conf import settings


process_log = logging.getLogger("main")


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDBSerializer

    def get_serializer_class(self):
        if settings.DB_TYPE == IN_MEMORY:
            return TaskInMemorySerializer.get_list_data()
        elif settings.DB_TYPE == MAIN_DB:
            return TaskDBSerializer
        else:
            return super().get_serializer_class(self)

    def list(self, request, *args, **kwargs):
        if settings.DB_TYPE == MAIN_DB:
            return super().list(self, request, *args, **kwargs)
        return Response(self.get_serializer_class())


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDBSerializer

    def get_serializer_class(self):
        if settings.DB_TYPE == IN_MEMORY:
            return TaskInMemorySerializer.get_list_data()
        elif settings.DB_TYPE == MAIN_DB:
            return TaskDBSerializer
        else:
            return super().get_serializer_class(self)

    def create(self, request, *args, **kwargs):
        if settings.DB_TYPE == MAIN_DB:
            return super().create(self, request, *args, **kwargs)

        list_repo = self.get_serializer_class()
        if not request.data or not request.data.get("title") or not request.data.get("body"):
            process_log.error("Invalid data has been received!")
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid data has been received!"})
        new_task = {"id": len(list_repo) + 1, "title": "t-01", "body": "desc-01"}
        list_repo.append(new_task)
        return Response(new_task)


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskDBSerializer
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if settings.DB_TYPE == IN_MEMORY:
            return TaskInMemorySerializer.get_list_data()
        elif settings.DB_TYPE == MAIN_DB:
            return TaskDBSerializer
        else:
            return super().get_serializer_class(self)

    def update(self, request, pk, *args, **kwargs):
        if settings.DB_TYPE == MAIN_DB:
            return super().update(self, request, pk, *args, **kwargs)
        list_repo = self.get_serializer_class()
        for each in list_repo:
            if each.get("id") == pk:
                each["title"] = request.data.get("title")
                each["body"] = request.data.get("body")
                return Response(each)
        process_log.error("Invalid id has been received!")
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Invalid id has been received!"})
