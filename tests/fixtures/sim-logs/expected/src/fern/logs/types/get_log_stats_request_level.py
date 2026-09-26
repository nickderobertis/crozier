

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLogStatsRequestLevel(enum.StrEnum):
    """
    Severity level to include.
    """

    INFO = "info"
    ERROR = "error"

    def visit(self, info: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetLogStatsRequestLevel.INFO:
            return info()
        if self is GetLogStatsRequestLevel.ERROR:
            return error()
