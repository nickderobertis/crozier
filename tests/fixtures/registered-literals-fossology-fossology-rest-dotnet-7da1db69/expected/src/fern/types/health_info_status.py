

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthInfoStatus(enum.StrEnum):
    """
    Status of service
    """

    OK = "OK"
    WARN = "WARN"
    ERROR = "ERROR"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HealthInfoStatus.OK:
            return ok()
        if self is HealthInfoStatus.WARN:
            return warn()
        if self is HealthInfoStatus.ERROR:
            return error()
