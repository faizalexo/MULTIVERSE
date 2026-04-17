from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='courses/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # 🔥 NEW → category (subject type)
    category = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)

            # 🔥 UNIQUE slug logic
            slug = base_slug
            counter = 1
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def total_lessons(self):
        return self.lessons.count()

    def total_quizzes(self):
        return self.quizzes.count()

    def total_videos(self):
        return self.videos.count()  # 🔥 NEW

    def __str__(self):
        return self.title


# 🔥 NEW MODEL → YouTube Videos
class Video(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='videos'
    )

    title = models.CharField(max_length=200)

    youtube_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # 🔥 YouTube embed link
    def embed_url(self):
        if "watch?v=" in self.youtube_url:
            return self.youtube_url.replace("watch?v=", "embed/")
        return self.youtube_url