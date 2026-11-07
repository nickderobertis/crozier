

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Severity(enum.StrEnum):
    CRITICAL = "CRITICAL"
    WARNING = "WARNING"
    INFO = "INFO"

    def visit(
        self,
        critical: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Severity.CRITICAL:
            return critical()
        if self is Severity.WARNING:
            return warning()
        if self is Severity.INFO:
            return info()
