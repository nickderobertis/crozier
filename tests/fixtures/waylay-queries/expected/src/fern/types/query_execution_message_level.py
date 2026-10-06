

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryExecutionMessageLevel(enum.StrEnum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryExecutionMessageLevel.DEBUG:
            return debug()
        if self is QueryExecutionMessageLevel.INFO:
            return info()
        if self is QueryExecutionMessageLevel.WARNING:
            return warning()
        if self is QueryExecutionMessageLevel.ERROR:
            return error()
