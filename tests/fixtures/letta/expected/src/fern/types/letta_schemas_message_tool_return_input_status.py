

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LettaSchemasMessageToolReturnInputStatus(enum.StrEnum):
    """
    The status of the tool call
    """

    SUCCESS = "success"
    ERROR = "error"

    def visit(self, success: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is LettaSchemasMessageToolReturnInputStatus.SUCCESS:
            return success()
        if self is LettaSchemasMessageToolReturnInputStatus.ERROR:
            return error()
