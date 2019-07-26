from django.db import models
from .utils import LogEntryLevelChoices


class LogEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Log Entries'
    project_id = models.IntegerField()
    level = models.IntegerField(choices=LogEntryLevelChoices)
    title = models.CharField(max_length=100)
    message = models.TextField()
