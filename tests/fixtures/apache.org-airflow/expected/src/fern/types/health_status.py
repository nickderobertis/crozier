

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthStatus(enum.StrEnum):
    """
    Health status
    """

    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def visit(self, healthy: typing.Callable[[], T_Result], unhealthy: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthStatus.HEALTHY:
            return healthy()
        if self is HealthStatus.UNHEALTHY:
            return unhealthy()
