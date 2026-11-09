

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsRelativeTimeRangeDtoV2TimeRange(enum.StrEnum):
    FIFTEEN_M = "15m"
    ONE_H = "1h"
    SIX_H = "6h"
    TWELVE_H = "12h"
    TWENTY_FOUR_H = "24h"
    SEVEN_D = "7d"
    THIRTY_D = "30d"
    CURRENT_WEEK = "current_week"
    CURRENT_MONTH = "current_month"
    PREVIOUS_WEEK = "previous_week"
    PREVIOUS_MONTH = "previous_month"

    def visit(
        self,
        fifteen_m: typing.Callable[[], T_Result],
        one_h: typing.Callable[[], T_Result],
        six_h: typing.Callable[[], T_Result],
        twelve_h: typing.Callable[[], T_Result],
        twenty_four_h: typing.Callable[[], T_Result],
        seven_d: typing.Callable[[], T_Result],
        thirty_d: typing.Callable[[], T_Result],
        current_week: typing.Callable[[], T_Result],
        current_month: typing.Callable[[], T_Result],
        previous_week: typing.Callable[[], T_Result],
        previous_month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.FIFTEEN_M:
            return fifteen_m()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.ONE_H:
            return one_h()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.SIX_H:
            return six_h()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.TWELVE_H:
            return twelve_h()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.TWENTY_FOUR_H:
            return twenty_four_h()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.SEVEN_D:
            return seven_d()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.THIRTY_D:
            return thirty_d()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.CURRENT_WEEK:
            return current_week()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.CURRENT_MONTH:
            return current_month()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.PREVIOUS_WEEK:
            return previous_week()
        if self is MetricsRelativeTimeRangeDtoV2TimeRange.PREVIOUS_MONTH:
            return previous_month()
