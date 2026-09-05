

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionMessageToolCallType(enum.StrEnum):
    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionMessageToolCallType.FUNCTION:
            return function()
