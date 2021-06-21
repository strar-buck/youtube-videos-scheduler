from django.conf.urls import url, include

urlpatterns = [
    url(r"^youtube-video/", include("youtube.urls")),
]
