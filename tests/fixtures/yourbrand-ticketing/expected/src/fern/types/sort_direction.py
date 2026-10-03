

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SortDirection(enum.StrEnum):
    """ """

    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortDirection.ASCENDING:
            return ascending()
        if self is SortDirection.DESCENDING:
            return descending()
