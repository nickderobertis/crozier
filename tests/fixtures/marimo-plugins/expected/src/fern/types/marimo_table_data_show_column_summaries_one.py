

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoTableDataShowColumnSummariesOne(enum.StrEnum):
    STATS = "stats"
    CHART = "chart"

    def visit(self, stats: typing.Callable[[], T_Result], chart: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoTableDataShowColumnSummariesOne.STATS:
            return stats()
        if self is MarimoTableDataShowColumnSummariesOne.CHART:
            return chart()
