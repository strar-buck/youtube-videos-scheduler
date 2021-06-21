from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fampay.settings")

app = Celery("fampay", namespace="CELERY")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(settings.INSTALLED_APPS)


# Running Tasks Periodically at interval of 10 sec
app.conf.beat_schedule = {
    "YOUTUBE_VIDEO_SCHEDULER": {
        "task": "youtube.tasks.fetchYoutubeVideos",
        "schedule": 10.00,
    }
}
