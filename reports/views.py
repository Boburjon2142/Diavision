from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from reminders.models import Reminder
from tracker.models import SugarReading

from .services import build_public_report_preview, build_user_reports


def public_reports(request):
    return render(request, "reports/public_reports.html", build_public_report_preview())


@login_required
def reports_dashboard(request):
    readings = SugarReading.objects.filter(user=request.user)[:30]
    reminders = Reminder.objects.filter(user=request.user, state="completed")[:30]
    weekly, monthly = build_user_reports(readings, reminders)
    return render(request, "reports/dashboard.html", {"weekly": weekly, "monthly": monthly})


@login_required
def printable_report(request, period):
    readings = SugarReading.objects.filter(user=request.user)[:30]
    reminders = Reminder.objects.filter(user=request.user, state="completed")[:30]
    weekly, monthly = build_user_reports(readings, reminders)
    report = weekly if period == "weekly" else monthly
    return render(request, "reports/printable.html", {"report": report, "period": period})
