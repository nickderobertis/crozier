

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemFieldsTarget(enum.StrEnum):
    """
    How the link opens
    """

    NEWTAB = "newtab"
    SAMETAB = "sametab"
    PARENT = "parent"
    TOP = "top"
    MODAL = "modal"
    WORKSPACE = "workspace"
    CLIPBOARD = "clipboard"
    NEWWINDOW = "newwindow"

    def visit(
        self,
        newtab: typing.Callable[[], T_Result],
        sametab: typing.Callable[[], T_Result],
        parent: typing.Callable[[], T_Result],
        top: typing.Callable[[], T_Result],
        modal: typing.Callable[[], T_Result],
        workspace: typing.Callable[[], T_Result],
        clipboard: typing.Callable[[], T_Result],
        newwindow: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ItemFieldsTarget.NEWTAB:
            return newtab()
        if self is ItemFieldsTarget.SAMETAB:
            return sametab()
        if self is ItemFieldsTarget.PARENT:
            return parent()
        if self is ItemFieldsTarget.TOP:
            return top()
        if self is ItemFieldsTarget.MODAL:
            return modal()
        if self is ItemFieldsTarget.WORKSPACE:
            return workspace()
        if self is ItemFieldsTarget.CLIPBOARD:
            return clipboard()
        if self is ItemFieldsTarget.NEWWINDOW:
            return newwindow()
