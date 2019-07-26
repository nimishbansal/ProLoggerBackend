from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from Project.models import LogEntry


@admin.register(LogEntry)
class LogEntryModelAdmin(ModelAdmin):
    list_display = ('project_id', 'title', 'message', 'level')
    list_filter = ('project_id',)
