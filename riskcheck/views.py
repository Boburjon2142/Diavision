from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RiskAssessmentForm
from .models import RiskAssessment, RiskFactorDetail
from .services import run_risk_assessment


def public_check(request):
    result = None
    if request.method == "POST":
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            result = run_risk_assessment(form.cleaned_data)
    else:
        form = RiskAssessmentForm()
    return render(request, "riskcheck/public_check.html", {"form": form, "result": result})


@login_required
def assessment_create(request):
    if request.method == "POST":
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            result = run_risk_assessment(form.cleaned_data)
            assessment = form.save(commit=False)
            assessment.user = request.user
            assessment.bmi = form.cleaned_data["bmi"]
            assessment.risk_level = result["risk_level"]
            assessment.risk_percentage = result["risk_percentage"]
            assessment.ai_explanation = result["explanation"]
            assessment.recommendations = result["recommendations_text"]
            assessment.next_steps = result["next_steps"]
            assessment.warning_text = result["warning"]
            assessment.save()
            for factor in result["factors"]:
                RiskFactorDetail.objects.create(
                    assessment=assessment,
                    factor_name=factor["name"],
                    factor_score=factor["score"],
                    factor_reason=factor["reason"],
                )
            messages.success(request, "AI xavf tahlili saqlandi.")
            return redirect("riskcheck:detail", pk=assessment.pk)
    else:
        form = RiskAssessmentForm()
    return render(request, "riskcheck/assessment_form.html", {"form": form})


@login_required
def detail(request, pk):
    assessment = RiskAssessment.objects.prefetch_related("risk_factors").get(pk=pk, user=request.user)
    return render(request, "riskcheck/detail.html", {"assessment": assessment})
