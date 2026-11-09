

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuditEventDtoSeverity(enum.StrEnum):
    """
    Severity level of the event
    """

    ERROR = "ERROR"
    INFO = "INFO"
    WARN = "WARN"
    DEBUG = "DEBUG"

    def visit(
        self,
        error: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        debug: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuditEventDtoSeverity.ERROR:
            return error()
        if self is AuditEventDtoSeverity.INFO:
            return info()
        if self is AuditEventDtoSeverity.WARN:
            return warn()
        if self is AuditEventDtoSeverity.DEBUG:
            return debug()
