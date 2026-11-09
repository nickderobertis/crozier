

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunToolCallObjectType(enum.StrEnum):
    """
    The type of tool call the output is required for. For now, this is always `function`.
    """

    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunToolCallObjectType.FUNCTION:
            return function()
