import requests
from twilio.rest import Client
from decouple import config

PROVIDER_TWILIO = 'twilio'
PROVIDER_FAST_TO_SMS = 'fast2sms'

twilio_account_sid = config("TWILIO_ACCOUNT_SID")
twilio_auth_token = config("TWILIO_AUTH_TOKEN")
twilio_client = Client(twilio_account_sid, twilio_auth_token)


def send_sms_from_twilio(to='+919654422849', body="empty_message"):
    message = twilio_client.messages.create(body=body, from_='+18325485985', to=to)
    print(message.sid)


def send_sms_from_fast_2_sms(to=None, body="empty message"):
    if to is None:
        to = ['+919654422849']
    to = ','.join(to)  # get comma separated list of numbers
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message={body}&language=english&route=p&numbers={nos}".format(
        **{"body": body, "nos": to})
    headers = {
        'authorization': config("FAST2SMS_AUTH_KEY"),
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def send_sms(to, body="empty message", provider=PROVIDER_TWILIO):
    if provider == PROVIDER_TWILIO:
        send_sms_from_twilio(to[0], body)  # send to single user

    elif provider == PROVIDER_FAST_TO_SMS:
        send_sms_from_fast_2_sms(to, body)
