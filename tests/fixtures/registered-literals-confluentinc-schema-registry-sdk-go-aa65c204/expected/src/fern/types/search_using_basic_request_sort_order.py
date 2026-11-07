

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchUsingBasicRequestSortOrder(enum.StrEnum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchUsingBasicRequestSortOrder.ASCENDING:
            return ascending()
        if self is SearchUsingBasicRequestSortOrder.DESCENDING:
            return descending()
