from .serializers import YoutubeVideoSerializer
from utils.logger import logger
from .constants import VIDEOS_SAVED_SUCCESSFULLY


def saveYoutubeVideos(data):
    """Handle the validation at serializer level and save the data into db"""
    if isinstance(data, list):
        serializer = YoutubeVideoSerializer(data=data, many=True)
    else:
        serializer = YoutubeVideoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        logger.info(VIDEOS_SAVED_SUCCESSFULLY)
    else:
        logger.error(serializer.errors)
