from rest_framework import serializers

from .models import YoutubeVideo, YoutubeVideoCredential


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = "__all__"
