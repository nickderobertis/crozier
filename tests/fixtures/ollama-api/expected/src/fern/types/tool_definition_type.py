

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolDefinitionType(enum.StrEnum):
    """
    Type of tool (always `function`)
    """

    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToolDefinitionType.FUNCTION:
            return function()
