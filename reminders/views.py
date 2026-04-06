from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ReminderForm
from .models import Reminder
from .services import recommend_time_windows


@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user).order_by("remind_time")
    ai_note = recommend_time_windows(list(reminders))
    return render(request, "reminders/list.html", {"reminders": reminders, "ai_note": ai_note})


@login_required
def reminder_create(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.ai_reason = "AI sizga qulay vaqtlarni kundalik odatlaringizga qarab tavsiya qiladi."
            reminder.save()
            messages.success(request, "Eslatma saqlandi.")
            return redirect("reminders:list")
    else:
        form = ReminderForm()
    return render(request, "reminders/form.html", {"form": form})
