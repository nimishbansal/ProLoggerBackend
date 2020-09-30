import json

import redis
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
# from django_mysql.models import JSONField
from jsonfield import JSONField

from rest_framework.authtoken.models import Token

from socketio_app.views import sio, send_new_log_entry_event
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

def send_via_redis(instance, data):
    r = redis.StrictRedis()
    project = Project.objects.get(id=instance.project_id)
    token, _ = Token.objects.get_or_create(user=project.user)
    # we publish to onChat with suffix as token key
    if "onChat" + token.key in list(map(lambda x: x.decode("utf-8"), r.pubsub_channels())):
        r.publish(channel="onChat{}".format(token.key), message=json.dumps(data))


def send_via_socket(instance, data):
    project = Project.objects.get(id=instance.project_id)
    token, _ = Token.objects.get_or_create(user=project.user)
    # we publish to chat with suffix as token key
    send_new_log_entry_event(event_name="onChat{}".format(token.key), data=json.dumps(data))


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
    # print(instance.tags)
    # send_via_redis(instance, data)
    send_via_socket(instance, data)


@receiver(pre_save, sender=Project)
def project_pre_save_hook(sender, instance, **kwargs):
    instance.secret_key = get_random_string(length=10)
