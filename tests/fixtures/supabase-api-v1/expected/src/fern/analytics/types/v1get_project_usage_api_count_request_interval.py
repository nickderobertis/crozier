

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1GetProjectUsageApiCountRequestInterval(enum.StrEnum):
    FIFTEEN_MIN = "15min"
    THIRTY_MIN = "30min"
    ONE_HR = "1hr"
    THREE_HR = "3hr"
    ONE_DAY = "1day"
    THREE_DAY = "3day"
    SEVEN_DAY = "7day"

    def visit(
        self,
        fifteen_min: typing.Callable[[], T_Result],
        thirty_min: typing.Callable[[], T_Result],
        one_hr: typing.Callable[[], T_Result],
        three_hr: typing.Callable[[], T_Result],
        one_day: typing.Callable[[], T_Result],
        three_day: typing.Callable[[], T_Result],
        seven_day: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1GetProjectUsageApiCountRequestInterval.FIFTEEN_MIN:
            return fifteen_min()
        if self is V1GetProjectUsageApiCountRequestInterval.THIRTY_MIN:
            return thirty_min()
        if self is V1GetProjectUsageApiCountRequestInterval.ONE_HR:
            return one_hr()
        if self is V1GetProjectUsageApiCountRequestInterval.THREE_HR:
            return three_hr()
        if self is V1GetProjectUsageApiCountRequestInterval.ONE_DAY:
            return one_day()
        if self is V1GetProjectUsageApiCountRequestInterval.THREE_DAY:
            return three_day()
        if self is V1GetProjectUsageApiCountRequestInterval.SEVEN_DAY:
            return seven_day()
