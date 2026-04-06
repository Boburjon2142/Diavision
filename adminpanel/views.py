from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from pages.models import Article, DoctorRequest, FAQ
from reports.models import AIInsightLog, AlertLog
from riskcheck.models import RiskAssessment


@staff_member_required
def analytics_dashboard(request):
    assessments = RiskAssessment.objects.all()
    context = {
        "risk_counts": {
            "high": assessments.filter(risk_level="high").count(),
            "medium": assessments.filter(risk_level="medium").count(),
            "low": assessments.filter(risk_level="low").count(),
        },
        "alerts": AlertLog.objects.order_by("-created_at")[:10],
        "doctor_requests": DoctorRequest.objects.order_by("-created_at")[:10],
        "articles": Article.objects.count(),
        "faq_count": FAQ.objects.count(),
        "ai_logs": AIInsightLog.objects.count(),
    }
    return render(request, "adminpanel/analytics.html", context)
