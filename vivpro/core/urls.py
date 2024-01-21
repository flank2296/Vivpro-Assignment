from django.urls import path, include

from core.views.core_views import NormalizeMusicJson, ping
from core.views.music_tracks import (
    MusicTrackListView,
    RateMusicTrackView,
    SearchMusicTrackByTitle,
)

track_urls = [
    path("rate/<str:track_id>", RateMusicTrackView.as_view()),
    path("search-by-title/<str:title>", SearchMusicTrackByTitle.as_view()),
    path(
        "fetch-by-page/<int:page_no>/<int:force_fetch_all>",
        MusicTrackListView.as_view(),
    ),
]

core_urlpatterns = [
    path("ping", ping),
    path("normalize_json", NormalizeMusicJson.as_view()),
]

track_api_url_patterns = [path("tracks/", include(track_urls))]
