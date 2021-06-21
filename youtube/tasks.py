import requests

from celery import shared_task

from django.db import transaction
from django.db import IntegrityError

from .constants import (
    YOUTUBE_SEARCH_BASE_API_URL,
    DEFAULT_SEARCH_QUERY,
    MAX_QUERY_RESULTS,
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    VIDEOS_SAVED_SUCCESSFULLY,
)
from .models import YoutubeVideoCredential, YoutubeVideo
from .service import YoutubeApiService
from .serializers import YoutubeVideoSerializer
from .utils import saveYoutubeVideos
from utils.logger import logger


@shared_task
def fetchYoutubeVideos():
    serviceInstance = YoutubeApiService()
    apiKey = serviceInstance.getKey()
    res, status_code = serviceInstance.fetchVideos()

    if status_code == HTTP_403_FORBIDDEN:
        try:
            with transaction.atomic():
                YoutubeVideoCredential.objects.filter(api_key=apiKey).update(
                    status=YoutubeVideoCredential.EXHAUSTED
                )
        except Exception as e:
            logger.error(e)

    elif status_code == HTTP_200_OK:
        try:
            saveYoutubeVideos(res)
            logger.info(VIDEOS_SAVED_SUCCESSFULLY)
        except IntegrityError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)
    else:
        try:
            with transaction.atomic():
                YoutubeVideoCredential.objects.filter(api_key=apiKey).update(
                    status=YoutubeVideoCredential.DEACTIVATED
                )
        except Exception as e:
            logger.error(e)
