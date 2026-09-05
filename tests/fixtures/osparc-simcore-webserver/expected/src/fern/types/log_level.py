

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogLevel(enum.StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LogLevel.DEBUG:
            return debug()
        if self is LogLevel.INFO:
            return info()
        if self is LogLevel.WARNING:
            return warning()
        if self is LogLevel.ERROR:
            return error()
