

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthCheckStatus(enum.StrEnum):
    """
    The health status of the pipeline
    """

    OK = "OK"
    ERROR = "ERROR"
    IDLE = "IDLE"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        idle: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HealthCheckStatus.OK:
            return ok()
        if self is HealthCheckStatus.ERROR:
            return error()
        if self is HealthCheckStatus.IDLE:
            return idle()
