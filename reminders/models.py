from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class Reminder(TimeStampedModel):
    TYPES = [
        ("medicine", "Dori"),
        ("water", "Suv"),
        ("meal", "Ovqat"),
        ("walking", "Piyoda yurish"),
        ("sugar_check", "Shakar o‘lchovi"),
        ("doctor", "Shifokor ko‘rigi"),
    ]
    STATES = [("active", "Faol"), ("inactive", "Nofaol"), ("completed", "Bajarilgan")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reminders")
    title = models.CharField(max_length=120)
    reminder_type = models.CharField(max_length=30, choices=TYPES)
    remind_time = models.TimeField()
    note = models.TextField(blank=True)
    state = models.CharField(max_length=20, choices=STATES, default="active")
    ai_reason = models.TextField(blank=True)
