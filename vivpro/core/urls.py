from core.views import NormalizeMusicJson, ping
from django.urls import path

core_urlpatterns = [
    path("ping", ping),
    path("normalize_json", NormalizeMusicJson.as_view()),
]
