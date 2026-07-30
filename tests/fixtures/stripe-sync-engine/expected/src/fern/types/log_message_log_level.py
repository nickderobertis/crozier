

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogMessageLogLevel(enum.StrEnum):
    """
    Log severity level.
    """

    DEBUG = "debug"
    INFO = "info"
    WARN = "warn"
    ERROR = "error"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LogMessageLogLevel.DEBUG:
            return debug()
        if self is LogMessageLogLevel.INFO:
            return info()
        if self is LogMessageLogLevel.WARN:
            return warn()
        if self is LogMessageLogLevel.ERROR:
            return error()
