

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SortOrder(enum.StrEnum):
    """
    Specifies the sort order for the search results.
    """

    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortOrder.ASCENDING:
            return ascending()
        if self is SortOrder.DESCENDING:
            return descending()
