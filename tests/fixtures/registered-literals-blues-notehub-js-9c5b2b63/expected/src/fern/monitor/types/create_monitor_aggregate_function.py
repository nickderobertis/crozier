

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateMonitorAggregateFunction(enum.StrEnum):
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
        if self is CreateMonitorAggregateFunction.NONE:
            return none()
        if self is CreateMonitorAggregateFunction.SUM:
            return sum()
        if self is CreateMonitorAggregateFunction.AVERAGE:
            return average()
        if self is CreateMonitorAggregateFunction.MAX:
            return max()
        if self is CreateMonitorAggregateFunction.MIN:
            return min()
