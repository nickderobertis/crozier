

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class HealthStatus(str, enum.Enum):
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
