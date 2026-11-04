

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionMetricsChartName(enum.StrEnum):
    """
    Session metrics chart to return.
    """

    SESSIONS_OVER_TIME = "sessions_over_time"
    SESSIONS_COST_OVER_TIME = "sessions_cost_over_time"
    TURNS_OVER_TIME = "turns_over_time"

    def visit(
        self,
        sessions_over_time: typing.Callable[[], T_Result],
        sessions_cost_over_time: typing.Callable[[], T_Result],
        turns_over_time: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SessionMetricsChartName.SESSIONS_OVER_TIME:
            return sessions_over_time()
        if self is SessionMetricsChartName.SESSIONS_COST_OVER_TIME:
            return sessions_cost_over_time()
        if self is SessionMetricsChartName.TURNS_OVER_TIME:
            return turns_over_time()
