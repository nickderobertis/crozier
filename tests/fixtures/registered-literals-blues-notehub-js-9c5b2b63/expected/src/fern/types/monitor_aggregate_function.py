

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonitorAggregateFunction(enum.StrEnum):
    """
    Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]
    """

    NONE = "none"
    SUM = "sum"
    AVERAGE = "average"
    MAX = "max"
    MIN = "min"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        sum: typing.Callable[[], T_Result],
        average: typing.Callable[[], T_Result],
        max: typing.Callable[[], T_Result],
        min: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitorAggregateFunction.NONE:
            return none()
        if self is MonitorAggregateFunction.SUM:
            return sum()
        if self is MonitorAggregateFunction.AVERAGE:
            return average()
        if self is MonitorAggregateFunction.MAX:
            return max()
        if self is MonitorAggregateFunction.MIN:
            return min()
