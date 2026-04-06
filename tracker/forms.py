from django import forms

from .models import SugarReading


class SugarReadingForm(forms.ModelForm):
    class Meta:
        model = SugarReading
        fields = ["reading_type", "value", "measured_at", "notes"]
        widgets = {"measured_at": forms.DateTimeInput(attrs={"type": "datetime-local"})}
