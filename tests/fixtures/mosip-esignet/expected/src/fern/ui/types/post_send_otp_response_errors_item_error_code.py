

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostSendOtpResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION = "invalid_transaction"
    INVALID_TRANSACTION_ID = "invalid_transaction_id"
    INVALID_IDENTIFIER = "invalid_identifier"
    INVALID_OTP_CHANNEL = "invalid_otp_channel"
    INVALID_CAPTCHA = "invalid_captcha"
    SEND_OTP_FAILED = "send_otp_failed"
    UNKNOWN_ERROR = "unknown_error"

    def visit(
        self,
        invalid_transaction: typing.Callable[[], T_Result],
        invalid_transaction_id: typing.Callable[[], T_Result],
        invalid_identifier: typing.Callable[[], T_Result],
        invalid_otp_channel: typing.Callable[[], T_Result],
        invalid_captcha: typing.Callable[[], T_Result],
        send_otp_failed: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostSendOtpResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is PostSendOtpResponseErrorsItemErrorCode.INVALID_TRANSACTION_ID:
            return invalid_transaction_id()
        if self is PostSendOtpResponseErrorsItemErrorCode.INVALID_IDENTIFIER:
            return invalid_identifier()
        if self is PostSendOtpResponseErrorsItemErrorCode.INVALID_OTP_CHANNEL:
            return invalid_otp_channel()
        if self is PostSendOtpResponseErrorsItemErrorCode.INVALID_CAPTCHA:
            return invalid_captcha()
        if self is PostSendOtpResponseErrorsItemErrorCode.SEND_OTP_FAILED:
            return send_otp_failed()
        if self is PostSendOtpResponseErrorsItemErrorCode.UNKNOWN_ERROR:
            return unknown_error()
