

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemsLinkRel(enum.StrEnum):
    SELF = "self"
    ITEMS = "items"

    def visit(self, self_: typing.Callable[[], T_Result], items: typing.Callable[[], T_Result]) -> T_Result:
        if self is ItemsLinkRel.SELF:
            return self_()
        if self is ItemsLinkRel.ITEMS:
            return items()
