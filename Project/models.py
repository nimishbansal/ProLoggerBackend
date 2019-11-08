import json
import redis
import requests
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mysql.models import JSONField
from rest_framework.authtoken.models import Token

from .utils import LogEntryLevelChoices


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=200, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class LogEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Log Entries'

    project_id = models.IntegerField()
    level = models.IntegerField(choices=LogEntryLevelChoices)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
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
        "project_id": instance.project_id,
        "level": instance.level,
        "title": instance.title,
        "message": instance.message,
        "created_at": {
            'year': instance.created_at.year,
            'month': instance.created_at.month,
            'hour': instance.created_at.hour,
            'day': instance.created_at.day,
            'minute': instance.created_at.minute,
            'second': instance.created_at.second
        }
    }
    print(instance.tags)
    r = redis.StrictRedis()
    project = Project.objects.get(id=instance.project_id)
    token, _ = Token.objects.get_or_create(user=project.user)
    # we publish to onChat with suffix as token key
    if "onChat" + token.key in list(map(lambda x: x.decode("utf-8"), r.pubsub_channels())):
        r.publish(channel="onChat{}".format(token.key), message=json.dumps(data))
