from rest_framework.views import APIView

from django.http import JsonResponse
from django.middleware.csrf import rotate_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from core.models import MusicTrack


@csrf_exempt
def ping(request):
    rotate_token(request)
    return JsonResponse({"message": "pong"})


@method_decorator(csrf_exempt, name="dispatch")
class NormalizeMusicJson(APIView):
    """API which accepts unstructured json input, normalizes it and adds in MusicTrack table"""

    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        payload = request.data
        if not payload:
            raise Exception("Invalid payload passed for storing music tracks")

        instance_mapper = {}
        for col_name, values in payload.items():
            col_name = col_name if col_name != "class" else "class_field"

            for index, value in values.items():
                current_instance = instance_mapper.get(index) or MusicTrack()
                setattr(current_instance, col_name, value)
                setattr(current_instance, "index", index)
                instance_mapper.update({index: current_instance})

        MusicTrack.objects.bulk_create(instance_mapper.values())
        return JsonResponse({"message": "Inserted music tracks successfully!"})
