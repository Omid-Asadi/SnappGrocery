from django.db import models
from lib.model import BaseModel


class Task(BaseModel):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.pk
