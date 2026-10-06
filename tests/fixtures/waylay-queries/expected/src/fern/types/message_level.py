

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageLevel(enum.StrEnum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    FATAL = "fatal"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        fatal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageLevel.DEBUG:
            return debug()
        if self is MessageLevel.INFO:
            return info()
        if self is MessageLevel.WARNING:
            return warning()
        if self is MessageLevel.ERROR:
            return error()
        if self is MessageLevel.FATAL:
            return fatal()
