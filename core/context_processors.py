from django.urls import reverse_lazy


def platform_context(request):
    return {
        "platform_name": "DiaVision AI",
        "medical_disclaimer": (
            "Platforma tibbiy tashxis qo‘ymaydi va shifokor maslahatining o‘rnini bosmaydi."
        ),
        "public_nav": [
            {"title": "Bosh sahifa", "url": reverse_lazy("pages:home")},
            {"title": "Platforma haqida", "url": reverse_lazy("pages:about")},
            {"title": "AI Risk Check", "url": reverse_lazy("riskcheck:public_check")},
            {"title": "Shakar nazorati", "url": reverse_lazy("tracker:public_overview")},
            {"title": "AI Oziq-ovqat", "url": reverse_lazy("nutrition:assistant")},
            {"title": "Hisobotlar", "url": reverse_lazy("reports:public_reports")},
            {"title": "Profilaktika", "url": reverse_lazy("pages:tips")},
            {"title": "FAQ", "url": reverse_lazy("pages:faq")},
            {"title": "Aloqa", "url": reverse_lazy("pages:contact")},
        ],
    }
