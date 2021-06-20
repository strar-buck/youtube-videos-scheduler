from enum import Enum

from django.db import models
from django.contrib.postgres.fields import JSONField


class YouTubeBaseModel(models.Model):
	"""The Base Class for all the models we have."""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class KeyStatus(Enum):
	"""
    This is an abstract model that is explicitly used for Api key Status.
    """

    # Api key status
    ACTIVE = 1
    DEACTIVATED = 2
    QUOTA_EXHAUSTED = 3

    def __str__(self):
        return self._name_.lower()

class APIKey(YouTubeBaseModel):
	key = models.CharField(max_length=100)
	status = models.IntegerField(default=KeyStatus.ACTIVE)

	def __str__(self):
        return f"{self.key}: {self.status}"

    class Meta:
    	db_table = "api_key"
        verbose_name = "Api Key"
        verbose_name_plural = "Api Keys"

class YouTubeVideo(YouTubeBaseModel):
    video_id = models.CharField(max_length=100, primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateTimeField(null=True)
    thumbnails = JSONField(null=True)

    class Meta:
        db_table = "youtube_video"
        verbose_name = "Youtube Video"
        verbose_name_plural = "Youtube Videos"

    def __str__(self):
        return self.title
