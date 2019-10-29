import json

from rest_framework import serializers
from rest_framework.fields import JSONField

from Project.models import LogEntry, ExceptionStackTrace, Project
from utility.serializer_utils import DisplaySelectedFieldMixin, CompleteDateTimeSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name',)


class ExceptionStackTraceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ExceptionStackTrace


class LogEntryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        exclude = ('project_id', )


class LogEntrySerializer(DisplaySelectedFieldMixin, serializers.ModelSerializer):
    level_name = serializers.SerializerMethodField()
    created_at = CompleteDateTimeSerializer()
    stacktrace = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = LogEntry

    @staticmethod
    def get_level_name(obj):
        return obj.get_level_display()

    @staticmethod
    def get_stacktrace(obj):
        try:
            stacktrace = obj.stacktrace
            return ExceptionStackTraceSerializer(stacktrace).data
        except ExceptionStackTrace.DoesNotExist:
            return None
