

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolsToolNamePostError500ErrorCode(enum.StrEnum):
    EXECUTION_ERROR = "EXECUTION_ERROR"

    def visit(self, execution_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToolsToolNamePostError500ErrorCode.EXECUTION_ERROR:
            return execution_error()
