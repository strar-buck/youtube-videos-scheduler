from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from djangorestframework_camel_case.parser import CamelCaseJSONParser
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from django_filters import rest_framework as filters

from .models import YoutubeVideo
from .filters import YoutubeVideoFilter
from .serializers import YoutubeVideoSerializer
from utils.logger import logger
from utils.pagination import PaginationHandlerMixin


class YoutubeVideoList(APIView):
    parser_classes = [CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = YoutubeVideoFilter

    def get(self, request, format=None):
        queryset = YoutubeVideo.objects.all()
        query_params = request.query_params
        if query_params:
            queryset = self.filter_queryset(queryset)

        serializer = YoutubeVideoSerializer(queryset, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        key = self.request.query_params.get("sort_by")
        queryset = queryset.distinct()
        if key:
            return queryset.order_by(*([k.strip() for k in key.split(",")]))

        return queryset
