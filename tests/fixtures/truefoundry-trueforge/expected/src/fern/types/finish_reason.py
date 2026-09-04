

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FinishReason(enum.StrEnum):
    """
    Why the model stopped generating.
    """

    STOP = "stop"
    LENGTH = "length"
    TOOL_CALLS = "tool_calls"
    CONTENT_FILTER = "content_filter"
    FUNCTION_CALL = "function_call"

    def visit(
        self,
        stop: typing.Callable[[], T_Result],
        length: typing.Callable[[], T_Result],
        tool_calls: typing.Callable[[], T_Result],
        content_filter: typing.Callable[[], T_Result],
        function_call: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FinishReason.STOP:
            return stop()
        if self is FinishReason.LENGTH:
            return length()
        if self is FinishReason.TOOL_CALLS:
            return tool_calls()
        if self is FinishReason.CONTENT_FILTER:
            return content_filter()
        if self is FinishReason.FUNCTION_CALL:
            return function_call()
