

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HalLinkRole(enum.StrEnum):
    """
    Supported link and embedding roles in HAL representations.
    """

    SELF = "self"
    FIRST = "first"
    PREV = "prev"
    NEXT = "next"
    LAST = "last"
    EXECUTE = "execute"

    def visit(
        self,
        self_: typing.Callable[[], T_Result],
        first: typing.Callable[[], T_Result],
        prev: typing.Callable[[], T_Result],
        next: typing.Callable[[], T_Result],
        last: typing.Callable[[], T_Result],
        execute: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HalLinkRole.SELF:
            return self_()
        if self is HalLinkRole.FIRST:
            return first()
        if self is HalLinkRole.PREV:
            return prev()
        if self is HalLinkRole.NEXT:
            return next()
        if self is HalLinkRole.LAST:
            return last()
        if self is HalLinkRole.EXECUTE:
            return execute()
