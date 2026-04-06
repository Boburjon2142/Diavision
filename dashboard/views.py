from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ai_engine.services.alert_engine import AlertEngine
from ai_engine.services.habit_engine import LifestyleScorer
from pages.models import DoctorRequest
from reminders.models import Reminder
from reports.models import AIInsightLog
from reports.services import build_user_reports
from riskcheck.models import RiskAssessment
from tracker.models import SugarReading


@login_required
def overview(request):
    latest_assessment = RiskAssessment.objects.filter(user=request.user).prefetch_related("risk_factors").first()
    readings = list(SugarReading.objects.filter(user=request.user)[:14])
    reminders = list(Reminder.objects.filter(user=request.user)[:6])
    weekly, monthly = build_user_reports(readings, reminders)
    context = {
        "latest_assessment": latest_assessment,
        "readings": readings[:5],
        "reminders": reminders[:4],
        "weekly": weekly,
        "monthly": monthly,
        "alert_status": AlertEngine(readings, latest_assessment).current_status(),
        "lifestyle": LifestyleScorer(readings, reminders).score(),
        "insights": AIInsightLog.objects.filter(user=request.user)[:5],
        "doctor_request_count": DoctorRequest.objects.count(),
    }
    return render(request, "dashboard/overview.html", context)
