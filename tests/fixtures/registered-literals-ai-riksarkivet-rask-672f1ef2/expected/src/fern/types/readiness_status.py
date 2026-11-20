

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadinessStatus(enum.StrEnum):
    STARTING = "starting"
    READY = "ready"
    SHUTTING_DOWN = "shutting_down"
    DEGRADED = "degraded"

    def visit(
        self,
        starting: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        shutting_down: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReadinessStatus.STARTING:
            return starting()
        if self is ReadinessStatus.READY:
            return ready()
        if self is ReadinessStatus.SHUTTING_DOWN:
            return shutting_down()
        if self is ReadinessStatus.DEGRADED:
            return degraded()
