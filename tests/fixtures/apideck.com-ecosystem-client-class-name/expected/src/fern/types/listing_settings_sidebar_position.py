

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListingSettingsSidebarPosition(enum.StrEnum):
    TOP = "TOP"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    HIDDEN = "HIDDEN"

    def visit(
        self,
        top: typing.Callable[[], T_Result],
        left: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
        hidden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListingSettingsSidebarPosition.TOP:
            return top()
        if self is ListingSettingsSidebarPosition.LEFT:
            return left()
        if self is ListingSettingsSidebarPosition.RIGHT:
            return right()
        if self is ListingSettingsSidebarPosition.HIDDEN:
            return hidden()
