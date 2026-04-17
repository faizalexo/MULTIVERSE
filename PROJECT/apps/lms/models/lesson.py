from django.db import models
import re


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    content = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_preview = models.BooleanField(default=False)

    video_url = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['order']
        unique_together = ['course', 'order']  # 🔥 important

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    def get_embed_url(self):
        if not self.video_url:
            return ""

        regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
        match = re.search(regex, self.video_url)

        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"

        return self.video_url