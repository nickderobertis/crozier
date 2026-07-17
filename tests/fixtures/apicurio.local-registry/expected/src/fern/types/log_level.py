

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogLevel(enum.StrEnum):
    """ """

    DEBUG = "DEBUG"
    TRACE = "TRACE"
    WARN = "WARN"
    ERROR = "ERROR"
    SEVERE = "SEVERE"
    WARNING = "WARNING"
    INFO = "INFO"
    CONFIG = "CONFIG"
    FINE = "FINE"
    FINER = "FINER"
    FINEST = "FINEST"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        trace: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        severe: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        config: typing.Callable[[], T_Result],
        fine: typing.Callable[[], T_Result],
        finer: typing.Callable[[], T_Result],
        finest: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LogLevel.DEBUG:
            return debug()
        if self is LogLevel.TRACE:
            return trace()
        if self is LogLevel.WARN:
            return warn()
        if self is LogLevel.ERROR:
            return error()
        if self is LogLevel.SEVERE:
            return severe()
        if self is LogLevel.WARNING:
            return warning()
        if self is LogLevel.INFO:
            return info()
        if self is LogLevel.CONFIG:
            return config()
        if self is LogLevel.FINE:
            return fine()
        if self is LogLevel.FINER:
            return finer()
        if self is LogLevel.FINEST:
            return finest()
