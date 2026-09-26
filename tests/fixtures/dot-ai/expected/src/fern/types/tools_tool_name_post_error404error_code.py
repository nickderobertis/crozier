

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolsToolNamePostError404ErrorCode(enum.StrEnum):
    TOOL_NOT_FOUND = "TOOL_NOT_FOUND"

    def visit(self, tool_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToolsToolNamePostError404ErrorCode.TOOL_NOT_FOUND:
            return tool_not_found()
