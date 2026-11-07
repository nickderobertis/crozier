

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchEntityAuditEventsRequestSeverity(enum.StrEnum):
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
        if self is SearchEntityAuditEventsRequestSeverity.ERROR:
            return error()
        if self is SearchEntityAuditEventsRequestSeverity.INFO:
            return info()
        if self is SearchEntityAuditEventsRequestSeverity.WARN:
            return warn()
        if self is SearchEntityAuditEventsRequestSeverity.DEBUG:
            return debug()
