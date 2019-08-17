from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from Project.models import LogEntry, ExceptionStackTrace


@admin.register(LogEntry)
class LogEntryModelAdmin(ModelAdmin):
    list_display = ('id', 'project_id', 'title', 'message', 'level')
    list_filter = ('id', 'project_id',)


@admin.register(ExceptionStackTrace)
class ExceptionStackTraceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'log_entry', 'frames_data')
