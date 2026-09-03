

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthStatusStatus(enum.StrEnum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def visit(self, healthy: typing.Callable[[], T_Result], unhealthy: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthStatusStatus.HEALTHY:
            return healthy()
        if self is HealthStatusStatus.UNHEALTHY:
            return unhealthy()
