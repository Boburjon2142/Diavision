from django.contrib import messages
from django.shortcuts import redirect, render

from pages.forms import ContactForm, DoctorRequestForm
from pages.models import Article, FAQ
from reports.services import build_public_report_preview


def home(request):
    articles = Article.objects.filter(is_published=True, featured=True)[:3]
    context = {
        "articles": articles,
        "hero_stats": [
            {"value": "24/7", "label": "AI monitoring faol"},
            {"value": "3 bosqich", "label": "Xavf tahlili, kuzatuv, tavsiya"},
            {"value": "100%", "label": "Mobil-first xizmat ko‘rsatish"},
        ],
        "report_preview": build_public_report_preview(),
    }
    return render(request, "pages/home.html", context)


def about(request):
    return render(request, "pages/about.html")


def tips(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, "pages/tips.html", {"articles": articles})


def faq(request):
    faq_items = FAQ.objects.filter(is_active=True)
    return render(request, "pages/faq.html", {"faq_items": faq_items})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Murojaatingiz qabul qilindi. Tez orada aloqaga chiqamiz.")
            return redirect("pages:contact")
    else:
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})


def doctor_connect(request):
    if request.method == "POST":
        form = DoctorRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Shifokor bilan bog‘lanish so‘rovi yuborildi.")
            return redirect("pages:doctor_connect")
    else:
        form = DoctorRequestForm()
    return render(request, "pages/doctor_connect.html", {"form": form})
