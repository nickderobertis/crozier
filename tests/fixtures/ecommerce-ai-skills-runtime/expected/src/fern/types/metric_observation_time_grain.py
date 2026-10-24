

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricObservationTimeGrain(enum.StrEnum):
    """
    snapshot is a point-in-time balance, day is one calendar day, and range uses the explicit period_start/period_end interval.
    """

    SNAPSHOT = "snapshot"
    DAY = "day"
    RANGE = "range"

    def visit(
        self,
        snapshot: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        range: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricObservationTimeGrain.SNAPSHOT:
            return snapshot()
        if self is MetricObservationTimeGrain.DAY:
            return day()
        if self is MetricObservationTimeGrain.RANGE:
            return range()
