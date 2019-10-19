STATUS = 'status'
SUCCESS = 'success'
ERROR = 'error'
MESSAGE = 'message'
ERROR_CODE = 'error_code'
OTP_MESSAGE = 'Hi, Your One Time Password(OTP) for ProLogger is {key}'

EXPIRED = 'expired'
NO_OTP = 'no_otp'
INVALID = 'invalid'

OTP_ERROR_CODES_MESSAGE = {
    EXPIRED: 'Otp has been expired.',
    NO_OTP: 'No such otp exists for this phone no.',
    INVALID: 'Otp provided is invalid'
}


def get_error_response_data(status, error_code):
    return {STATUS: status, ERROR_CODE: error_code, MESSAGE: OTP_ERROR_CODES_MESSAGE[error_code]}
