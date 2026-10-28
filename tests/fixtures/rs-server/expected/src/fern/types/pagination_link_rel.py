

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaginationLinkRel(enum.StrEnum):
    NEXT = "next"
    PREV = "prev"

    def visit(self, next: typing.Callable[[], T_Result], prev: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaginationLinkRel.NEXT:
            return next()
        if self is PaginationLinkRel.PREV:
            return prev()
