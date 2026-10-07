

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SqlParseErrorSeverity(enum.StrEnum):
    ERROR = "error"
    WARNING = "warning"

    def visit(self, error: typing.Callable[[], T_Result], warning: typing.Callable[[], T_Result]) -> T_Result:
        if self is SqlParseErrorSeverity.ERROR:
            return error()
        if self is SqlParseErrorSeverity.WARNING:
            return warning()
