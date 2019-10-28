import random

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Common.models import OTP
from Common.utils import SUCCESS, STATUS, ERROR, MESSAGE, ERROR_CODE, NO_OTP, OTP_ERROR_CODES_MESSAGE, \
    get_error_response_data, EXPIRED, INVALID


@api_view(('POST',))
@permission_classes((AllowAny,))
def send_otp(request):
    otp = OTP.objects.filter(phone_no=request.data['phone_no']).first()
    key = random.randint(1000, 9999)
    if otp:
        otp.key = key
        otp.save()
    else:
        OTP.objects.create(phone_no=request.data['phone_no'], key=key)
    return Response(data={STATUS: SUCCESS})


@api_view(('POST',))
@permission_classes((AllowAny,))
def verify_otp(request):
    error_code = None
    otp = OTP.objects.filter(phone_no=request.data['phone_no']).first()
    if otp is None:
        error_code = NO_OTP

    else:
        if otp.is_expired():
            error_code = EXPIRED
        elif str(otp.key) != request.data['key']:
            error_code = INVALID
        else:
            user = User.objects.filter(username=otp.phone_no).first()
            if user is None:
                user = User.objects.create_user(username=str(otp.phone_no),
                                                password=User.objects.make_random_password(length=10))
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={STATUS: SUCCESS, 'key': token.key})

    if error_code is not None:
        return Response(data=get_error_response_data(error_code=error_code, status=ERROR),
                        status=status.HTTP_400_BAD_REQUEST)
