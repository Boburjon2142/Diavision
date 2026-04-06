from django.db import models

from core.models import TimeStampedModel


class Article(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField()
    body = models.TextField()
    category = models.CharField(max_length=120, default="Profilaktika")
    is_published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FAQ(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.question


class DoctorRequest(TimeStampedModel):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    region = models.CharField(max_length=120)
    note = models.TextField(blank=True)
    status = models.CharField(max_length=30, default="new")

    def __str__(self):
        return f"{self.full_name} - {self.region}"
