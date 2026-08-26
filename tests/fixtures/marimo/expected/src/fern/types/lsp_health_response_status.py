

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LspHealthResponseStatus(enum.StrEnum):
    DEGRADED = "degraded"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def visit(
        self,
        degraded: typing.Callable[[], T_Result],
        healthy: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LspHealthResponseStatus.DEGRADED:
            return degraded()
        if self is LspHealthResponseStatus.HEALTHY:
            return healthy()
        if self is LspHealthResponseStatus.UNHEALTHY:
            return unhealthy()
