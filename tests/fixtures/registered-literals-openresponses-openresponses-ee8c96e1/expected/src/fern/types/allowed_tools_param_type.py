

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedToolsParamType(enum.StrEnum):
    """
    The tool choice type. Always `allowed_tools`.
    """

    ALLOWED_TOOLS = "allowed_tools"

    def visit(self, allowed_tools: typing.Callable[[], T_Result]) -> T_Result:
        if self is AllowedToolsParamType.ALLOWED_TOOLS:
            return allowed_tools()
