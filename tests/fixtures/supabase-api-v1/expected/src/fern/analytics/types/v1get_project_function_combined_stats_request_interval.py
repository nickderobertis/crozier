

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1GetProjectFunctionCombinedStatsRequestInterval(enum.StrEnum):
    FIFTEEN_MIN = "15min"
    ONE_HR = "1hr"
    THREE_HR = "3hr"
    ONE_DAY = "1day"

    def visit(
        self,
        fifteen_min: typing.Callable[[], T_Result],
        one_hr: typing.Callable[[], T_Result],
        three_hr: typing.Callable[[], T_Result],
        one_day: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1GetProjectFunctionCombinedStatsRequestInterval.FIFTEEN_MIN:
            return fifteen_min()
        if self is V1GetProjectFunctionCombinedStatsRequestInterval.ONE_HR:
            return one_hr()
        if self is V1GetProjectFunctionCombinedStatsRequestInterval.THREE_HR:
            return three_hr()
        if self is V1GetProjectFunctionCombinedStatsRequestInterval.ONE_DAY:
            return one_day()
