from functools import partial

import time
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination

from ..api.serializers import LogEntrySerializer
from ..models import LogEntry


class StandardPagination(PageNumberPagination):
    page_size = 10


class LogEntryListView(ListAPIView):
    pagination_class = StandardPagination
    serializer_class = partial(LogEntrySerializer, exclude_fields=[])

    def get_queryset(self):
        return LogEntry.objects.filter(project_id=self.kwargs['project_id']).order_by('-id')


class LogEntryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = partial(LogEntrySerializer, exclude_fields=['project_id'])
    queryset = LogEntry.objects.all()

    def get_object(self):
        return get_object_or_404(LogEntry.objects.using('default'), project_id=self.kwargs['project_id'],
                                 id=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        time.sleep(5)
        return super(LogEntryRetrieveUpdateDestroyView, self).delete(request, *args, **kwargs)

def sample(request):
    a = 40
    b = 50
    print('hehehe')
    print(a/(b-50))
    print("hahahah")
    print('hohoho')
    return