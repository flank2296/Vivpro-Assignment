from rest_framework import serializers

from core.models import MusicTrack


class MusicSerializer(serializers.ModelSerializer):
    duration_seconds = serializers.SerializerMethodField()

    class Meta:
        model = MusicTrack
        fields = "__all__"

    def get_duration_seconds(self, instance):
        """Converts duration ms to seconds"""
        if not instance.duration_ms:
            return instance.duration_ms

        return instance.duration_ms / 1000
