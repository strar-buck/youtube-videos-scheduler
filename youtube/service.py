from datetime import datetime
import requests

from .models import YoutubeVideoCredential
from .constants import (
    YOUTUBE_SEARCH_BASE_API_URL,
    DEFAULT_SEARCH_QUERY,
    MAX_QUERY_RESULTS,
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    ACTIVE_API_KEY_NOT_FOUND,
    DEACTIVATED_API_KEY,
    EXHAUSTED_API_KEY,
)
from utils.functions import getAuthorizationHeaders, formatDateTime
from utils.logger import logger


class YoutubeApiService(object):
    def __init__(self):
        self.apiKey = YoutubeVideoCredential.getKey()
        self.videoSearchUrl = YOUTUBE_SEARCH_BASE_API_URL
        self.searchQuery = DEFAULT_SEARCH_QUERY
        self.maxResults = MAX_QUERY_RESULTS

    def getKey(self):
        return self.apiKey

    def fetchVideos(self):
        """Fetch youtube Videos through youtube api"""
        if not self.apiKey:
            logger.error(ACTIVE_API_KEY_NOT_FOUND)
            return ACTIVE_API_KEY_NOT_FOUND, HTTP_403_FORBIDDEN

        queryParams = dict(
            part="snippet",
            q=self.searchQuery,
            maxResults=self.maxResults,
            key=self.apiKey,
            type="video",
            order="date",
        )

        headers = getAuthorizationHeaders()
        response = requests.get(
            YOUTUBE_SEARCH_BASE_API_URL, headers=headers, params=queryParams
        )
        json_response = response.json()
        if response.status_code == HTTP_403_FORBIDDEN:
            return EXHAUSTED_API_KEY, HTTP_403_FORBIDDEN

        elif response.status_code == HTTP_200_OK:
            videoList = json_response.get("items", [])
            youTubeVideos = []
            for video in videoList:
                videoDetails = dict()
                snippetDetail = video.get("snippet")
                videoDetails["video_id"] = video.get("id").get("videoId")
                videoDetails["video_title"] = snippetDetail.get("title")
                videoDetails["thumbnail"] = snippetDetail.get("thumbnails")
                videoDetails["description"] = snippetDetail.get("description")
                videoDetails["channel_id"] = snippetDetail.get("channelId")
                videoDetails["channel_title"] = snippetDetail.get("channelTitle")
                videoDetails["published_at"] = formatDateTime(
                    snippetDetail.get("publishedAt")
                )

                youTubeVideos.append(videoDetails)
            return youTubeVideos, HTTP_200_OK
        else:
            return DEACTIVATED_API_KEY, HTTP_401_UNAUTHORIZED
