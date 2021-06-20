from django.db import models
from django.contrib.postgres.fields import JSONField


class YouTubeBaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
