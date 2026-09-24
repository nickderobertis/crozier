

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogFileHandlerLevel(enum.StrEnum):
    """
    The global log level for the application
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
        if self is LogFileHandlerLevel.DEBUG:
            return debug()
        if self is LogFileHandlerLevel.INFO:
            return info()
        if self is LogFileHandlerLevel.WARN:
            return warn()
        if self is LogFileHandlerLevel.ERROR:
            return error()
