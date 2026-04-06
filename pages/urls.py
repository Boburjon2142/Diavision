from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("tips/", views.tips, name="tips"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
    path("doctor-connect/", views.doctor_connect, name="doctor_connect"),
]
