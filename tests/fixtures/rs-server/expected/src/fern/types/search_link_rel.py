

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchLinkRel(enum.StrEnum):
    SELF = "self"
    SEARCH = "search"
    NEXT = "next"
    PREV = "prev"

    def visit(
        self,
        self_: typing.Callable[[], T_Result],
        search: typing.Callable[[], T_Result],
        next: typing.Callable[[], T_Result],
        prev: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchLinkRel.SELF:
            return self_()
        if self is SearchLinkRel.SEARCH:
            return search()
        if self is SearchLinkRel.NEXT:
            return next()
        if self is SearchLinkRel.PREV:
            return prev()
