

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BriefingMetricTimeGrain(enum.StrEnum):
    SNAPSHOT = "snapshot"
    DAY = "day"
    RANGE = "range"

    def visit(
        self,
        snapshot: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        range: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BriefingMetricTimeGrain.SNAPSHOT:
            return snapshot()
        if self is BriefingMetricTimeGrain.DAY:
            return day()
        if self is BriefingMetricTimeGrain.RANGE:
            return range()
