

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostBindingOtpResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_OTP_CHANNEL = "invalid_otp_channel"
    UNKNOWN_ERROR = "unknown_error"
    INVALID_INDIVIDUAL_ID = "invalid_individual_id"
    SEND_OTP_FAILED = "send_otp_failed"
    INVALID_CAPTCHA = "invalid_captcha"

    def visit(
        self,
        invalid_otp_channel: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
        invalid_individual_id: typing.Callable[[], T_Result],
        send_otp_failed: typing.Callable[[], T_Result],
        invalid_captcha: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostBindingOtpResponseErrorsItemErrorCode.INVALID_OTP_CHANNEL:
            return invalid_otp_channel()
        if self is PostBindingOtpResponseErrorsItemErrorCode.UNKNOWN_ERROR:
            return unknown_error()
        if self is PostBindingOtpResponseErrorsItemErrorCode.INVALID_INDIVIDUAL_ID:
            return invalid_individual_id()
        if self is PostBindingOtpResponseErrorsItemErrorCode.SEND_OTP_FAILED:
            return send_otp_failed()
        if self is PostBindingOtpResponseErrorsItemErrorCode.INVALID_CAPTCHA:
            return invalid_captcha()
