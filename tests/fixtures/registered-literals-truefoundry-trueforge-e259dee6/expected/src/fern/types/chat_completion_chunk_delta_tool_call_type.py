

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionChunkDeltaToolCallType(enum.StrEnum):
    """
    Tool call type when present on this delta.
    """

    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionChunkDeltaToolCallType.FUNCTION:
            return function()
