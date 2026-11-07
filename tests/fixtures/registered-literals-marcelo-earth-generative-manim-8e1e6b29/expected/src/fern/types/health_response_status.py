

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthResponseStatus(enum.StrEnum):
    """
    healthy if at least one provider key is configured, degraded otherwise.
    """

    HEALTHY = "healthy"
    DEGRADED = "degraded"

    def visit(self, healthy: typing.Callable[[], T_Result], degraded: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthResponseStatus.HEALTHY:
            return healthy()
        if self is HealthResponseStatus.DEGRADED:
            return degraded()
