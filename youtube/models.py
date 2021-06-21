from django.db import models
from django.contrib.postgres.fields import JSONField


class YoutubeBaseModel(models.Model):
    """The Base Class for all the models we have."""

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class YoutubeVideoCredential(YoutubeBaseModel):
    ACTIVE = "active"
    DEACTIVATED = "deactivated"
    EXHAUSTED = "exhausted"

    KEY_STATUS_CHOICES = (
        (ACTIVE, "active"),
        (DEACTIVATED, "deactivated"),
        (EXHAUSTED, "exhausted"),
    )
    api_key = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=KEY_STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return f"{self.api_key}: {self.status}"

    class Meta:
        db_table = "api_key"
        verbose_name = "Api Key"
        verbose_name_plural = "Api Keys"

    @classmethod
    def getKey(cls):
        key_instance = YoutubeVideoCredential.objects.filter(status=cls.ACTIVE).first()
        return key_instance.api_key if key_instance else None


class YoutubeVideo(YoutubeBaseModel):
    video_id = models.CharField(max_length=100, primary_key=True, unique=True)
    video_title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True)
    thumbnails = JSONField(null=True)
    channel_id = models.CharField(max_length=100)
    channel_title = models.CharField(max_length=200)

    class Meta:
        db_table = "youtube_video"
        verbose_name = "Youtube Video"
        verbose_name_plural = "Youtube Videos"

    def __str__(self):
        return self.video_title
