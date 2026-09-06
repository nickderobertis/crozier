

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TimeOnPageReportsRequestTimeseriesGranularityPeriod(enum.StrEnum):
    """
    Bucket size for a time on page timeseries. `day` returns one value per day and `week` returns one value per week.
    """

    DAY = "day"
    WEEK = "week"

    def visit(self, day: typing.Callable[[], T_Result], week: typing.Callable[[], T_Result]) -> T_Result:
        if self is TimeOnPageReportsRequestTimeseriesGranularityPeriod.DAY:
            return day()
        if self is TimeOnPageReportsRequestTimeseriesGranularityPeriod.WEEK:
            return week()
