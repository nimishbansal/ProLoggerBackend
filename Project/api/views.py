from django.core.paginator import Paginator
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination, BasePagination

from ..api.serializers import LogEntrySerializer
from ..models import LogEntry


class StandardPagination(PageNumberPagination):
    page_size = 10


class LogEntryListView(ListAPIView):
    pagination_class = StandardPagination
    serializer_class = LogEntrySerializer

    def get_queryset(self):
        return LogEntry.objects.filter(project_id=self.kwargs['project_id'])
