

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Operator(enum.StrEnum):
    """
    Defines the set of operators supported by the API.
    """

    EQ = "eq"
    NE = "ne"
    NEQ = "neq"
    LT = "lt"
    LTE = "lte"
    GT = "gt"
    GTE = "gte"

    def visit(
        self,
        eq: typing.Callable[[], T_Result],
        ne: typing.Callable[[], T_Result],
        neq: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
        gt: typing.Callable[[], T_Result],
        gte: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Operator.EQ:
            return eq()
        if self is Operator.NE:
            return ne()
        if self is Operator.NEQ:
            return neq()
        if self is Operator.LT:
            return lt()
        if self is Operator.LTE:
            return lte()
        if self is Operator.GT:
            return gt()
        if self is Operator.GTE:
            return gte()
