

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InsightsGetJobTimeseriesDataRequestGranularity(enum.StrEnum):
    DAILY = "daily"
    HOURLY = "hourly"

    def visit(self, daily: typing.Callable[[], T_Result], hourly: typing.Callable[[], T_Result]) -> T_Result:
        if self is InsightsGetJobTimeseriesDataRequestGranularity.DAILY:
            return daily()
        if self is InsightsGetJobTimeseriesDataRequestGranularity.HOURLY:
            return hourly()
