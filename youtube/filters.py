from utils.model_tools import make_model_filter
from .models import YoutubeVideo


def videos_search_on_title(self, qs, name, value):
    return qs.filter(video_title__icontains=value)


def videos_search_on_description(self, qs, name, value):
    return qs.filter(description__icontains=value)


youTubeVideosFilter = {
    "title": videos_search_on_title,
    "description": videos_search_on_description,
}

YoutubeVideoFilter = make_model_filter(YoutubeVideo, **youTubeVideosFilter)
