

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ServiceHealthResponseOutputStatus(enum.StrEnum):
    COMING_UP = "COMING_UP"
    ACTIVE_HEALTHY = "ACTIVE_HEALTHY"
    UNHEALTHY = "UNHEALTHY"

    def visit(
        self,
        coming_up: typing.Callable[[], T_Result],
        active_healthy: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ServiceHealthResponseOutputStatus.COMING_UP:
            return coming_up()
        if self is V1ServiceHealthResponseOutputStatus.ACTIVE_HEALTHY:
            return active_healthy()
        if self is V1ServiceHealthResponseOutputStatus.UNHEALTHY:
            return unhealthy()
