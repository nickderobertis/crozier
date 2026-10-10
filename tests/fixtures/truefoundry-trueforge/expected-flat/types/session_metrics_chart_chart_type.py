

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionMetricsChartChartType(enum.StrEnum):
    LINE = "line"

    def visit(self, line: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionMetricsChartChartType.LINE:
            return line()
