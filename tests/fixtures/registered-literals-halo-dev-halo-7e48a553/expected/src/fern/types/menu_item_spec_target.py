

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MenuItemSpecTarget(enum.StrEnum):
    """
    HTML anchor target used by the menu item.
    """

    BLANK = "_blank"
    SELF = "_self"
    PARENT = "_parent"
    TOP = "_top"

    def visit(
        self,
        blank: typing.Callable[[], T_Result],
        self_: typing.Callable[[], T_Result],
        parent: typing.Callable[[], T_Result],
        top: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MenuItemSpecTarget.BLANK:
            return blank()
        if self is MenuItemSpecTarget.SELF:
            return self_()
        if self is MenuItemSpecTarget.PARENT:
            return parent()
        if self is MenuItemSpecTarget.TOP:
            return top()
