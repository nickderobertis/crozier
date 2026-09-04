

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobHistorySummaryResultState(enum.StrEnum):
    WAITING = "waiting"
    READY = "ready"
    INCOMPLETE = "incomplete"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        waiting: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobHistorySummaryResultState.WAITING:
            return waiting()
        if self is JobHistorySummaryResultState.READY:
            return ready()
        if self is JobHistorySummaryResultState.INCOMPLETE:
            return incomplete()
        if self is JobHistorySummaryResultState.UNAVAILABLE:
            return unavailable()
