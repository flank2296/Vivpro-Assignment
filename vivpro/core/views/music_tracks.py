import json

from rest_framework.views import APIView

from django.http import JsonResponse

from core.models import MusicTrack
from core.serializer import MusicSerializer


class MusicTrackListView(APIView):
    """API which returns music list. supports pagiantion"""

    http_method_names = ["get"]
    MAX_ITEM_SIZE = 10

    def get(self, request, page_no, *args, **kwargs):
        to_idx = page_no * self.MAX_ITEM_SIZE
        from_idx = to_idx - self.MAX_ITEM_SIZE

        instances = MusicTrack.objects.all()
        total_instaces = instances.count()
        sliced_instances = instances[from_idx:to_idx]
        return JsonResponse(
            {
                "current_page": page_no,
                "is_last_page": total_instaces <= to_idx,
                "no_of_pages": total_instaces / (to_idx - from_idx),
                "instaces": MusicSerializer(sliced_instances, many=True).data,
            }
        )


class SearchMusicTrackByTitle(APIView):
    """API to search music track by using title of the song"""

    http_method_names = ["get"]

    def get(self, request, title, *args, **kwargs):
        if not title:
            raise Exception("Invalid title passed for searching a song!")

        return JsonResponse(
            {
                "tracks": MusicSerializer(
                    MusicTrack.objects.filter(title__contains=title), many=True
                ).data
            }
        )


class RateMusicTrackView(APIView):
    """API which is used for rating a music track"""

    http_method_names = ["post"]

    def post(self, request, track_id, *args, **kwargs):
        rating = (request.data or {}).get("rating")
        if rating is None:
            raise Exception("Invalid rating passed!")

        try:
            track = MusicTrack.objects.get(pk=track_id)
        except MusicTrack.DoesNotExist:
            raise Exception(
                "Invalid music track id passed! Such track does not exists!"
            )

        track.rating = rating
        track.save()
        return JsonResponse({"message": "Rating has been updated successfully!"})
