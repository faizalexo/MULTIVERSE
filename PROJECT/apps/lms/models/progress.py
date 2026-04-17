from django.db import models
from django.contrib.auth.models import User
from .course import Course
from .lesson import Lesson


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # ✅ category अलग field होना चाहिए
    category = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # Track completed lessons properly
    completed_lessons = models.ManyToManyField(Lesson, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

    def progress_percentage(self):
        total = self.course.lessons.count()
        completed = self.completed_lessons.count()

        if total == 0:
            return 0

        return int((completed / total) * 100)