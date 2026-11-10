

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FineTuningJobEventLevel(enum.StrEnum):
    INFO = "info"
    WARN = "warn"
    ERROR = "error"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FineTuningJobEventLevel.INFO:
            return info()
        if self is FineTuningJobEventLevel.WARN:
            return warn()
        if self is FineTuningJobEventLevel.ERROR:
            return error()
