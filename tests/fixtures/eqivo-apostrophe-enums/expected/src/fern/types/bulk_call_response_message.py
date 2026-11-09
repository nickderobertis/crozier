

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BulkCallResponseMessage(enum.StrEnum):
    """
    Response message
    """

    BULK_CALLS_REQUEST_EXECUTED = "BulkCalls Request Executed"
    MANDATORY_PARAMETERS_MISSING = "Mandatory Parameters Missing"
    THIS_DELIMITER_IS_NOT_ALLOWED = "This Delimiter is not allowed"
    BULK_CALLS_SHOULD_BE_USED_FOR_AT_LEAST2NUMBERS = "BulkCalls should be used for at least 2 numbers"
    TO_PARAMETER_LENGTH_DOES_NOT_MATCH_GATEWAYS_LENGTH = "'To' parameter length does not match 'Gateways' Length"
    ANSWER_URL_IS_NOT_VALID = "AnswerUrl is not Valid"
    HANGUP_URL_IS_NOT_VALID = "HangupUrl is not Valid"
    RING_URL_IS_NOT_VALID = "RingUrl is not Valid"
    UNKNOWN_CORE_UUID = "Unknown Core UUID"

    def visit(
        self,
        bulk_calls_request_executed: typing.Callable[[], T_Result],
        mandatory_parameters_missing: typing.Callable[[], T_Result],
        this_delimiter_is_not_allowed: typing.Callable[[], T_Result],
        bulk_calls_should_be_used_for_at_least2numbers: typing.Callable[[], T_Result],
        to_parameter_length_does_not_match_gateways_length: typing.Callable[[], T_Result],
        answer_url_is_not_valid: typing.Callable[[], T_Result],
        hangup_url_is_not_valid: typing.Callable[[], T_Result],
        ring_url_is_not_valid: typing.Callable[[], T_Result],
        unknown_core_uuid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BulkCallResponseMessage.BULK_CALLS_REQUEST_EXECUTED:
            return bulk_calls_request_executed()
        if self is BulkCallResponseMessage.MANDATORY_PARAMETERS_MISSING:
            return mandatory_parameters_missing()
        if self is BulkCallResponseMessage.THIS_DELIMITER_IS_NOT_ALLOWED:
            return this_delimiter_is_not_allowed()
        if self is BulkCallResponseMessage.BULK_CALLS_SHOULD_BE_USED_FOR_AT_LEAST2NUMBERS:
            return bulk_calls_should_be_used_for_at_least2numbers()
        if self is BulkCallResponseMessage.TO_PARAMETER_LENGTH_DOES_NOT_MATCH_GATEWAYS_LENGTH:
            return to_parameter_length_does_not_match_gateways_length()
        if self is BulkCallResponseMessage.ANSWER_URL_IS_NOT_VALID:
            return answer_url_is_not_valid()
        if self is BulkCallResponseMessage.HANGUP_URL_IS_NOT_VALID:
            return hangup_url_is_not_valid()
        if self is BulkCallResponseMessage.RING_URL_IS_NOT_VALID:
            return ring_url_is_not_valid()
        if self is BulkCallResponseMessage.UNKNOWN_CORE_UUID:
            return unknown_core_uuid()
