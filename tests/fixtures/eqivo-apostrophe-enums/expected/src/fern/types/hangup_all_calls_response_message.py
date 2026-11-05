

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HangupAllCallsResponseMessage(enum.StrEnum):
    """
    Response message
    """

    ALL_CALLS_HUNGUP = "All Calls Hungup"
    HANGUP_CALL_FAILED = "Hangup Call Failed"

    def visit(
        self, all_calls_hungup: typing.Callable[[], T_Result], hangup_call_failed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is HangupAllCallsResponseMessage.ALL_CALLS_HUNGUP:
            return all_calls_hungup()
        if self is HangupAllCallsResponseMessage.HANGUP_CALL_FAILED:
            return hangup_call_failed()
