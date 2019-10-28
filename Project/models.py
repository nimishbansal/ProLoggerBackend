import json

import requests
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mysql.models import JSONField

from .utils import LogEntryLevelChoices


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class LogEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Log Entries'

    project_id = models.IntegerField()
    level = models.IntegerField(choices=LogEntryLevelChoices)
    title = models.CharField(max_length=100)
    message = models.TextField()
    tags = JSONField(null=True, blank=True, default=dict)
    created_at = models.DateTimeField(auto_now_add=True)


class ExceptionStackTrace(models.Model):
    log_entry = models.OneToOneField(LogEntry, on_delete=models.CASCADE, related_name='stacktrace')
    frames_data = JSONField(null=True, blank=True)


# @receiver(post_save, sender=LogEntry, dispatch_uid="log_entry_saved")
# def log_entry_post_save_hook(sender, instance, created, **kwargs):
#     if created:
#         ExceptionStackTrace(log_entry=instance).save()

@receiver(post_save, sender=LogEntry, dispatch_uid="log_entry_saved")
def log_entry_post_save_hook(sender, instance, **kwargs):
    data = {
        "id": instance.id,
        "level_name": instance.get_level_display(),
        "project_id": 1,
        "level": instance.level,
        "title": instance.title,
        "message": instance.message
    }
    print(data)
    requests.post("http://0.0.0.0:8080/newevent/", data=json.dumps(data))
