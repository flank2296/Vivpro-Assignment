from django.http import JsonResponse
from django.middleware.csrf import rotate_token
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def ping(request):
    rotate_token(request)
    return JsonResponse({"message": "pong"})
