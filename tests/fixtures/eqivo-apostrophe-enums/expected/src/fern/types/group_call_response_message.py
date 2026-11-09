

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GroupCallResponseMessage(enum.StrEnum):
    """
    Response message
    """

    GROUP_CALL_REQUEST_EXECUTED = "GroupCall Request Executed"
    MANDATORY_PARAMETERS_MISSING = "Mandatory Parameters Missing"
    THIS_DELIMITER_IS_NOT_ALLOWED = "This Delimiter is not allowed"
    GROUP_CALL_SHOULD_BE_USED_FOR_AT_LEAST2NUMBERS = "GroupCall should be used for at least 2 numbers"
    TO_PARAMETER_LENGTH_DOES_NOT_MATCH_GATEWAYS_LENGTH = "'To' parameter length does not match 'Gateways' Length"
    ANSWER_URL_IS_NOT_VALID = "AnswerUrl is not Valid"
    HANGUP_URL_IS_NOT_VALID = "HangupUrl is not Valid"
    RING_URL_IS_NOT_VALID = "RingUrl is not Valid"
    CONFIRM_SOUND_IS_NOT_VALID = "ConfirmSound is not Valid"
    UNKNOWN_CORE_UUID = "Unknown Core UUID"
    GROUP_CALL_REQUEST_FAILED = "GroupCall Request Failed"

    def visit(
        self,
        group_call_request_executed: typing.Callable[[], T_Result],
        mandatory_parameters_missing: typing.Callable[[], T_Result],
        this_delimiter_is_not_allowed: typing.Callable[[], T_Result],
        group_call_should_be_used_for_at_least2numbers: typing.Callable[[], T_Result],
        to_parameter_length_does_not_match_gateways_length: typing.Callable[[], T_Result],
        answer_url_is_not_valid: typing.Callable[[], T_Result],
        hangup_url_is_not_valid: typing.Callable[[], T_Result],
        ring_url_is_not_valid: typing.Callable[[], T_Result],
        confirm_sound_is_not_valid: typing.Callable[[], T_Result],
        unknown_core_uuid: typing.Callable[[], T_Result],
        group_call_request_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GroupCallResponseMessage.GROUP_CALL_REQUEST_EXECUTED:
            return group_call_request_executed()
        if self is GroupCallResponseMessage.MANDATORY_PARAMETERS_MISSING:
            return mandatory_parameters_missing()
        if self is GroupCallResponseMessage.THIS_DELIMITER_IS_NOT_ALLOWED:
            return this_delimiter_is_not_allowed()
        if self is GroupCallResponseMessage.GROUP_CALL_SHOULD_BE_USED_FOR_AT_LEAST2NUMBERS:
            return group_call_should_be_used_for_at_least2numbers()
        if self is GroupCallResponseMessage.TO_PARAMETER_LENGTH_DOES_NOT_MATCH_GATEWAYS_LENGTH:
            return to_parameter_length_does_not_match_gateways_length()
        if self is GroupCallResponseMessage.ANSWER_URL_IS_NOT_VALID:
            return answer_url_is_not_valid()
        if self is GroupCallResponseMessage.HANGUP_URL_IS_NOT_VALID:
            return hangup_url_is_not_valid()
        if self is GroupCallResponseMessage.RING_URL_IS_NOT_VALID:
            return ring_url_is_not_valid()
        if self is GroupCallResponseMessage.CONFIRM_SOUND_IS_NOT_VALID:
            return confirm_sound_is_not_valid()
        if self is GroupCallResponseMessage.UNKNOWN_CORE_UUID:
            return unknown_core_uuid()
        if self is GroupCallResponseMessage.GROUP_CALL_REQUEST_FAILED:
            return group_call_request_failed()
