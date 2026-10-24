

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotRuntimeStatusStatus(enum.StrEnum):
    STARTING = "starting"
    HEALTHY = "healthy"
    STALE = "stale"
    DEGRADED = "degraded"
    STOPPING = "stopping"
    STOPPED = "stopped"
    SUPERSEDED = "superseded"

    def visit(
        self,
        starting: typing.Callable[[], T_Result],
        healthy: typing.Callable[[], T_Result],
        stale: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        superseded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PilotRuntimeStatusStatus.STARTING:
            return starting()
        if self is PilotRuntimeStatusStatus.HEALTHY:
            return healthy()
        if self is PilotRuntimeStatusStatus.STALE:
            return stale()
        if self is PilotRuntimeStatusStatus.DEGRADED:
            return degraded()
        if self is PilotRuntimeStatusStatus.STOPPING:
            return stopping()
        if self is PilotRuntimeStatusStatus.STOPPED:
            return stopped()
        if self is PilotRuntimeStatusStatus.SUPERSEDED:
            return superseded()
