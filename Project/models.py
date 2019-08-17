from django.db import models
from django_mysql.models import JSONField

from .utils import LogEntryLevelChoices


class LogEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Log Entries'

    project_id = models.IntegerField()
    level = models.IntegerField(choices=LogEntryLevelChoices)
    title = models.CharField(max_length=100)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


class ExceptionStackTrace(models.Model):
    log_entry = models.OneToOneField(LogEntry, on_delete=models.CASCADE, related_name='stacktrace')
    frames_data = JSONField(null=True, blank=True)


# @receiver(post_save, sender=LogEntry, dispatch_uid="log_entry_saved")
# def log_entry_post_save_hook(sender, instance, created, **kwargs):
#     if created:
#         ExceptionStackTrace(log_entry=instance).save()
