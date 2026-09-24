

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogConsoleHandlerLevel(enum.StrEnum):
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
        if self is LogConsoleHandlerLevel.DEBUG:
            return debug()
        if self is LogConsoleHandlerLevel.INFO:
            return info()
        if self is LogConsoleHandlerLevel.WARN:
            return warn()
        if self is LogConsoleHandlerLevel.ERROR:
            return error()
