

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolsToolNamePostError400ErrorCode(enum.StrEnum):
    INVALID_REQUEST = "INVALID_REQUEST"

    def visit(self, invalid_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToolsToolNamePostError400ErrorCode.INVALID_REQUEST:
            return invalid_request()
