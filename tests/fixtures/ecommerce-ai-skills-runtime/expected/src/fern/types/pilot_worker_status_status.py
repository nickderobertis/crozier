

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotWorkerStatusStatus(enum.StrEnum):
    STARTING = "starting"
    HEALTHY = "healthy"
    STALE = "stale"
    DEGRADED = "degraded"
    STOPPED = "stopped"

    def visit(
        self,
        starting: typing.Callable[[], T_Result],
        healthy: typing.Callable[[], T_Result],
        stale: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PilotWorkerStatusStatus.STARTING:
            return starting()
        if self is PilotWorkerStatusStatus.HEALTHY:
            return healthy()
        if self is PilotWorkerStatusStatus.STALE:
            return stale()
        if self is PilotWorkerStatusStatus.DEGRADED:
            return degraded()
        if self is PilotWorkerStatusStatus.STOPPED:
            return stopped()
