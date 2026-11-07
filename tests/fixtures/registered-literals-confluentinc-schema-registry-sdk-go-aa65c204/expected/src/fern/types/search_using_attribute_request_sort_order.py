

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchUsingAttributeRequestSortOrder(enum.StrEnum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchUsingAttributeRequestSortOrder.ASCENDING:
            return ascending()
        if self is SearchUsingAttributeRequestSortOrder.DESCENDING:
            return descending()
