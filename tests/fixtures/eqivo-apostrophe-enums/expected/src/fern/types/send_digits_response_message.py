

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SendDigitsResponseMessage(enum.StrEnum):
    """
    Response message
    """

    SEND_DIGITS_EXECUTED = "SendDigits Executed"
    CALL_UUID_PARAMETER_MISSING = "CallUUID Parameter Missing"
    DIGITS_PARAMETER_MISSING = "Digits Parameter Missing"
    INVALID_LEG_PARAMETER = "Invalid Leg Parameter"
    SEND_DIGITS_FAILED_CALL_NOT_FOUND = "SendDigits Failed -- Call not found"
    SEND_DIGITS_FAILED = "SendDigits Failed"

    def visit(
        self,
        send_digits_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_missing: typing.Callable[[], T_Result],
        digits_parameter_missing: typing.Callable[[], T_Result],
        invalid_leg_parameter: typing.Callable[[], T_Result],
        send_digits_failed_call_not_found: typing.Callable[[], T_Result],
        send_digits_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SendDigitsResponseMessage.SEND_DIGITS_EXECUTED:
            return send_digits_executed()
        if self is SendDigitsResponseMessage.CALL_UUID_PARAMETER_MISSING:
            return call_uuid_parameter_missing()
        if self is SendDigitsResponseMessage.DIGITS_PARAMETER_MISSING:
            return digits_parameter_missing()
        if self is SendDigitsResponseMessage.INVALID_LEG_PARAMETER:
            return invalid_leg_parameter()
        if self is SendDigitsResponseMessage.SEND_DIGITS_FAILED_CALL_NOT_FOUND:
            return send_digits_failed_call_not_found()
        if self is SendDigitsResponseMessage.SEND_DIGITS_FAILED:
            return send_digits_failed()
