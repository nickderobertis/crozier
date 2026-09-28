

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadCheckComparator(enum.StrEnum):
    """
    how the observed value is compared to value: string comparators (EQUALS/NOT_EQUALS/CONTAINS/MATCHES — MATCHES is a full-match regex) operate on the raw string; numeric comparators (GT/LT/GTE/LTE) parse both sides as numbers and fail the check when either side is not a number
    """

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
        if self is LoadCheckComparator.EQUALS:
            return equals()
        if self is LoadCheckComparator.NOT_EQUALS:
            return not_equals()
        if self is LoadCheckComparator.CONTAINS:
            return contains()
        if self is LoadCheckComparator.MATCHES:
            return matches()
        if self is LoadCheckComparator.GT:
            return gt()
        if self is LoadCheckComparator.LT:
            return lt()
        if self is LoadCheckComparator.GTE:
            return gte()
        if self is LoadCheckComparator.LTE:
            return lte()
