

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionMetricsGraphChartType(enum.StrEnum):
    LINE = "line"

    def visit(self, line: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionMetricsGraphChartType.LINE:
            return line()
