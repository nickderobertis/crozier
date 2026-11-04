

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthResponseStatus(enum.StrEnum):
    """
    Current health state of the server:

    - `healthy`: Operational and processing requests
    - `starting`: Initializing (binding port, setting up routes)
    - `shutting_down`: Graceful shutdown in progress
    - `unhealthy`: Error state, requires restart
    """

    HEALTHY = "healthy"
    STARTING = "starting"
    SHUTTING_DOWN = "shutting_down"
    UNHEALTHY = "unhealthy"

    def visit(
        self,
        healthy: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        shutting_down: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HealthResponseStatus.HEALTHY:
            return healthy()
        if self is HealthResponseStatus.STARTING:
            return starting()
        if self is HealthResponseStatus.SHUTTING_DOWN:
            return shutting_down()
        if self is HealthResponseStatus.UNHEALTHY:
            return unhealthy()
