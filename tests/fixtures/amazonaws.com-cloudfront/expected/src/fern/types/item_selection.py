

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemSelection(enum.StrEnum):
    NONE = "none"
    WHITELIST = "whitelist"
    ALL = "all"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        whitelist: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ItemSelection.NONE:
            return none()
        if self is ItemSelection.WHITELIST:
            return whitelist()
        if self is ItemSelection.ALL:
            return all_()
