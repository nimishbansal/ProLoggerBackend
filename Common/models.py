from datetime import timedelta
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from Common.utils import OTP_MESSAGE
from utility.sms_utils import send_sms


class OTP(models.Model):
    phone_no = models.CharField(unique=True, max_length=16)
    key = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        if timezone.now() - self.timestamp > timedelta(minutes=2):
            return True
        else:
            return False

    is_expired.boolean = True


@receiver(post_save, sender=OTP, dispatch_uid="otp_saved")
def otp_post_save_hook(**kwargs):
    instance = kwargs['instance']
    print(instance.phone_no)
    send_sms(to=[instance.phone_no], body=OTP_MESSAGE.format(key=instance.key))
