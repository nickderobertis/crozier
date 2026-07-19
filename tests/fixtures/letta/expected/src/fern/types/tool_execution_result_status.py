

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolExecutionResultStatus(enum.StrEnum):
    """
    The status of the tool execution and return object
    """

    SUCCESS = "success"
    ERROR = "error"

    def visit(self, success: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToolExecutionResultStatus.SUCCESS:
            return success()
        if self is ToolExecutionResultStatus.ERROR:
            return error()
