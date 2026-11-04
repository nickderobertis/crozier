

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthResponseStatus(enum.StrEnum):
    OK = "ok"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HealthResponseStatus.OK:
            return ok()
        if self is HealthResponseStatus.DEGRADED:
            return degraded()
        if self is HealthResponseStatus.UNHEALTHY:
            return unhealthy()
