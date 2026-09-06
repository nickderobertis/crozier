

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Ordering(enum.StrEnum):
    """
    Defines the ordering in a listing of results.
    """

    ASCENDING = "ascending"
    DESCENDING = "descending"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is Ordering.ASCENDING:
            return ascending()
        if self is Ordering.DESCENDING:
            return descending()
