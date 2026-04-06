from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class FoodQueryHistory(TimeStampedModel):
    LABELS = [
        ("recommended", "Tavsiya etiladi"),
        ("caution", "Ehtiyot bilan"),
        ("avoid", "Tavsiya etilmaydi"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="food_queries")
    meal_name = models.CharField(max_length=120)
    label = models.CharField(max_length=20, choices=LABELS)
    portion_guidance = models.CharField(max_length=255)
    alternatives = models.TextField()
    ai_explanation = models.TextField()
