

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadCheckResultComparator(enum.StrEnum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    MATCHES = "MATCHES"
    GT = "GT"
    LT = "LT"
    GTE = "GTE"
    LTE = "LTE"

    def visit(
        self,
        equals: typing.Callable[[], T_Result],
        not_equals: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        matches: typing.Callable[[], T_Result],
        gt: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        gte: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadCheckResultComparator.EQUALS:
            return equals()
        if self is LoadCheckResultComparator.NOT_EQUALS:
            return not_equals()
        if self is LoadCheckResultComparator.CONTAINS:
            return contains()
        if self is LoadCheckResultComparator.MATCHES:
            return matches()
        if self is LoadCheckResultComparator.GT:
            return gt()
        if self is LoadCheckResultComparator.LT:
            return lt()
        if self is LoadCheckResultComparator.GTE:
            return gte()
        if self is LoadCheckResultComparator.LTE:
            return lte()
