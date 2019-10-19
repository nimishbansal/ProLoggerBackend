from django.contrib import admin

# Register your models here.
from Common.models import OTP


@admin.register(OTP)
class OTPModelAdmin(admin.ModelAdmin):
    search_fields = ('phone_no', )
    list_display = ('id', 'phone_no', 'key', 'timestamp', 'is_expired')
