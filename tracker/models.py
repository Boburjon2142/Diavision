from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class SugarReading(TimeStampedModel):
    READING_TYPES = [
        ("fasting", "Och qoringa"),
        ("before_meal", "Ovqatdan oldin"),
        ("after_meal", "Ovqatdan keyin"),
        ("evening", "Kechqurun"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sugar_readings")
    reading_type = models.CharField(max_length=20, choices=READING_TYPES)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    measured_at = models.DateTimeField()
    notes = models.TextField(blank=True)
    is_unusual = models.BooleanField(default=False)

    class Meta:
        ordering = ["-measured_at"]
