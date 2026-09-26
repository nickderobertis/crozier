

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogLevel(enum.StrEnum):
    """
    Log level
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LogLevel.DEBUG:
            return debug()
        if self is LogLevel.INFO:
            return info()
        if self is LogLevel.WARN:
            return warn()
        if self is LogLevel.ERROR:
            return error()
