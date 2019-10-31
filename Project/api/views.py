import traceback
from functools import partial

import time

from django.http import Http404
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, ListCreateAPIView, \
    GenericAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Common.utils import STATUS, SUCCESS, ERROR
from ..api.serializers import LogEntrySerializer, ProjectSerializer, LogEntryCreateSerializer
from ..models import LogEntry, Project
import logging


class ProjectSecretKeyVerificationView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            get_object_or_404(Project, secret_key=request.data['secret_key'])
            return Response({STATUS: SUCCESS})
        except Http404:
            return Response({STATUS: ERROR, 'message': 'No project found for this corresponding key'})


class LogEntryCreateView(CreateAPIView):
    serializer_class = LogEntryCreateSerializer
    project = None

    def create(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, secret_key=request.headers['Project-Token'])
        print(request.data)
        try:
            r = super(LogEntryCreateView, self).create(request, *args, **kwargs)
        except Exception as E:
            print("houu")
            print(E)
            traceback.print_exc()
            print("touu")
        # return Response({STATUS: SUCCESS})

    def perform_create(self, serializer):
        try:
            serializer.save(project_id=self.project.id)
        except Exception as E:
            print("error here")
            traceback.print_exc()


class StandardPagination(PageNumberPagination):
    page_size = 10


class ProjectListCreateView(ListCreateAPIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        time.sleep(1)
        return Project.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        print("Creating")
        serializer.save(user=self.request.user)


class ProjectBulkDeleteView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        Project.objects.filter(id__in=request.data).delete()
        return Response('', status=status.HTTP_204_NO_CONTENT)


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
        return super(LogEntryRetrieveUpdateDestroyView, self).delete(request, *args, **kwargs)


def sample(request):
    logging.getLogger('sentry_debug_logger').debug("haww", extra={"newtag": "ok"})
    a = 40
    b = 50
    print('hehehe')
    print(a / (b - 50))
    print("hahahah")
    print('hohoho')
    return
