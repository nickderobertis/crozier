

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReduceFunction(enum.StrEnum):
    LAST = "LAST"
    AVG = "AVG"
    MIN = "MIN"
    MAX = "MAX"
    SUM = "SUM"

    def visit(
        self,
        last: typing.Callable[[], T_Result],
        avg: typing.Callable[[], T_Result],
        min: typing.Callable[[], T_Result],
        max: typing.Callable[[], T_Result],
        sum: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReduceFunction.LAST:
            return last()
        if self is ReduceFunction.AVG:
            return avg()
        if self is ReduceFunction.MIN:
            return min()
        if self is ReduceFunction.MAX:
            return max()
        if self is ReduceFunction.SUM:
            return sum()
