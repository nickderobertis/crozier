

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CALL_REQUEST_EXECUTED = "Call Request Executed"
    MANDATORY_PARAMETERS_MISSING = "Mandatory Parameters Missing"
    ANSWER_URL_IS_NOT_VALID = "AnswerUrl is not Valid"
    HANGUP_URL_IS_NOT_VALID = "HangupUrl is not Valid"
    RING_URL_IS_NOT_VALID = "RingUrl is not Valid"
    UNKNOWN_CORE_UUID = "Unknown Core UUID"

    def visit(
        self,
        call_request_executed: typing.Callable[[], T_Result],
        mandatory_parameters_missing: typing.Callable[[], T_Result],
        answer_url_is_not_valid: typing.Callable[[], T_Result],
        hangup_url_is_not_valid: typing.Callable[[], T_Result],
        ring_url_is_not_valid: typing.Callable[[], T_Result],
        unknown_core_uuid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CallResponseMessage.CALL_REQUEST_EXECUTED:
            return call_request_executed()
        if self is CallResponseMessage.MANDATORY_PARAMETERS_MISSING:
            return mandatory_parameters_missing()
        if self is CallResponseMessage.ANSWER_URL_IS_NOT_VALID:
            return answer_url_is_not_valid()
        if self is CallResponseMessage.HANGUP_URL_IS_NOT_VALID:
            return hangup_url_is_not_valid()
        if self is CallResponseMessage.RING_URL_IS_NOT_VALID:
            return ring_url_is_not_valid()
        if self is CallResponseMessage.UNKNOWN_CORE_UUID:
            return unknown_core_uuid()
