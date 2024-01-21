from core.views import ping
from django.urls import path

core_urlpatterns = [
    path("ping/", ping),
]
