from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "DiaVision AI boshqaruv paneli"
admin.site.site_title = "DiaVision AI Admin"
admin.site.index_title = "Platforma boshqaruvi"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("risk/", include("riskcheck.urls")),
    path("tracker/", include("tracker.urls")),
    path("reminders/", include("reminders.urls")),
    path("nutrition/", include("nutrition.urls")),
    path("reports/", include("reports.urls")),
    path("management/", include("adminpanel.urls")),
    path("ai/", include("ai_engine.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
