

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppLogRequestLevel(enum.StrEnum):
    """
    Log level
    """

    DEBUG = "debug"
    INFO = "info"
    ERROR = "error"
    WARN = "warn"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppLogRequestLevel.DEBUG:
            return debug()
        if self is AppLogRequestLevel.INFO:
            return info()
        if self is AppLogRequestLevel.ERROR:
            return error()
        if self is AppLogRequestLevel.WARN:
            return warn()
