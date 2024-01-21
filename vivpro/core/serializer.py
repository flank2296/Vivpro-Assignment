from rest_framework.serializers import ModelSerializer

from core.models import MusicTrack


class MusicSerializer(ModelSerializer):
    class Meta:
        model = MusicTrack
        fields = "__all__"
