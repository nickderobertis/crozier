

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedToolChoiceType(enum.StrEnum):
    ALLOWED_TOOLS = "allowed_tools"

    def visit(self, allowed_tools: typing.Callable[[], T_Result]) -> T_Result:
        if self is AllowedToolChoiceType.ALLOWED_TOOLS:
            return allowed_tools()
