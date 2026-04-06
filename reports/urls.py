from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path("", views.public_reports, name="public_reports"),
    path("dashboard/", views.reports_dashboard, name="dashboard"),
    path("print/<str:period>/", views.printable_report, name="printable"),
]
