

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HangupCallResponseMessage(enum.StrEnum):
    """
    Response message
    """

    HANGUP_CALL_EXECUTED = "Hangup Call Executed"
    CALL_UUID_OR_REQUEST_UUID_PARAMETER_MUST_BE_PRESENT = "CallUUID or RequestUUID Parameter must be present"
    BOTH_CALL_UUID_AND_REQUEST_UUID_PARAMETERS_CANNOT_BE_PRESENT = (
        "Both CallUUID and RequestUUID Parameters cannot be present"
    )
    HANGUP_CALL_FAILED = "Hangup Call Failed"

    def visit(
        self,
        hangup_call_executed: typing.Callable[[], T_Result],
        call_uuid_or_request_uuid_parameter_must_be_present: typing.Callable[[], T_Result],
        both_call_uuid_and_request_uuid_parameters_cannot_be_present: typing.Callable[[], T_Result],
        hangup_call_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HangupCallResponseMessage.HANGUP_CALL_EXECUTED:
            return hangup_call_executed()
        if self is HangupCallResponseMessage.CALL_UUID_OR_REQUEST_UUID_PARAMETER_MUST_BE_PRESENT:
            return call_uuid_or_request_uuid_parameter_must_be_present()
        if self is HangupCallResponseMessage.BOTH_CALL_UUID_AND_REQUEST_UUID_PARAMETERS_CANNOT_BE_PRESENT:
            return both_call_uuid_and_request_uuid_parameters_cannot_be_present()
        if self is HangupCallResponseMessage.HANGUP_CALL_FAILED:
            return hangup_call_failed()
