from django.conf.urls import url, include
from .views import YoutubeVideoList

urlpatterns = [
    url(r"list", YoutubeVideoList.as_view(), name="youtubevideo-list",),
]
