

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SystemStatusStatus(enum.StrEnum):
    """
    The status of the system
    """

    NORMAL = "NORMAL"
    ERROR = "ERROR"

    def visit(self, normal: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is SystemStatusStatus.NORMAL:
            return normal()
        if self is SystemStatusStatus.ERROR:
            return error()
