

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthStatusStatus(enum.StrEnum):
    OK = "ok"
    DEGRADED = "degraded"

    def visit(self, ok: typing.Callable[[], T_Result], degraded: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthStatusStatus.OK:
            return ok()
        if self is HealthStatusStatus.DEGRADED:
            return degraded()
