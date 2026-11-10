

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionToolType(enum.StrEnum):
    """
    The type of the tool. Currently, only `function` is supported.
    """

    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionToolType.FUNCTION:
            return function()
