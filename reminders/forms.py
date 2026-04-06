from django import forms

from .models import Reminder


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ["title", "reminder_type", "remind_time", "note", "state"]
        widgets = {"remind_time": forms.TimeInput(attrs={"type": "time"})}
