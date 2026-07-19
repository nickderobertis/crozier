

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionMessageFunctionToolCallInputType(enum.StrEnum):
    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionMessageFunctionToolCallInputType.FUNCTION:
            return function()
