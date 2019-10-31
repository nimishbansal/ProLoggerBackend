from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from Project.models import LogEntry, ExceptionStackTrace, Project


@admin.register(Project)
class ProjectModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'user')


@admin.register(LogEntry)
class LogEntryModelAdmin(ModelAdmin):
    list_display = ('id', 'project_id', 'title', 'message', 'level', 'tags',)
    list_filter = ('id', 'project_id',)


@admin.register(ExceptionStackTrace)
class ExceptionStackTraceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'log_entry', 'frames_data')
