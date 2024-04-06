from django.urls import path
from task.api.views import TaskCreateView, TaskUpdateView, TaskListView


urlpatterns = [
    path("task-list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskUpdateView.as_view(), name="create-task"),
    path("task/", TaskCreateView.as_view(), name="update-task"),
]
