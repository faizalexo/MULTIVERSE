from django.db import models
from django.contrib.auth.models import User
from .lesson import Lesson

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)