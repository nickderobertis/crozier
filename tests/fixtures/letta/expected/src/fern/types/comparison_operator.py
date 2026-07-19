

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ComparisonOperator(enum.StrEnum):
    """
    Comparison operators for filtering numeric values
    """

    EQ = "eq"
    GTE = "gte"
    LTE = "lte"

    def visit(
        self, eq: typing.Callable[[], T_Result], gte: typing.Callable[[], T_Result], lte: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ComparisonOperator.EQ:
            return eq()
        if self is ComparisonOperator.GTE:
            return gte()
        if self is ComparisonOperator.LTE:
            return lte()
