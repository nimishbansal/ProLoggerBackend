from rest_framework import serializers

from Project.models import LogEntry
from utility.serializer_utils import DisplaySelectedFieldMixin


class LogEntrySerializer(DisplaySelectedFieldMixin, serializers.ModelSerializer):
    level_name = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = LogEntry

    @staticmethod
    def get_level_name(obj):
        return obj.get_level_display()
