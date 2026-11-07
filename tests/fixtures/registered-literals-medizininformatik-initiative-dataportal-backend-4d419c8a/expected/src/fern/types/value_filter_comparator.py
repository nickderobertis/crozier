

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValueFilterComparator(enum.StrEnum):
    EQ = "eq"
    UE = "ue"
    LE = "le"
    LT = "lt"
    GE = "ge"
    GT = "gt"

    def visit(
        self,
        eq: typing.Callable[[], T_Result],
        ue: typing.Callable[[], T_Result],
        le: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        ge: typing.Callable[[], T_Result],
        gt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValueFilterComparator.EQ:
            return eq()
        if self is ValueFilterComparator.UE:
            return ue()
        if self is ValueFilterComparator.LE:
            return le()
        if self is ValueFilterComparator.LT:
            return lt()
        if self is ValueFilterComparator.GE:
            return ge()
        if self is ValueFilterComparator.GT:
            return gt()
