

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CharterWindow(enum.StrEnum):
    """
    Charters never leave at slack water.
    """

    SLACK = "slack"
    FLOOD = "flood"
    EBB = "ebb"
    NEAP = "neap"

    def visit(
        self,
        slack: typing.Callable[[], T_Result],
        flood: typing.Callable[[], T_Result],
        ebb: typing.Callable[[], T_Result],
        neap: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CharterWindow.SLACK:
            return slack()
        if self is CharterWindow.FLOOD:
            return flood()
        if self is CharterWindow.EBB:
            return ebb()
        if self is CharterWindow.NEAP:
            return neap()
