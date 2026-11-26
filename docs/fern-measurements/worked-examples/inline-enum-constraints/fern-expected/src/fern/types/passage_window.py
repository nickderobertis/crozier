

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PassageWindow(enum.StrEnum):
    """
    Locks never open at slack water.
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
        if self is PassageWindow.SLACK:
            return slack()
        if self is PassageWindow.FLOOD:
            return flood()
        if self is PassageWindow.EBB:
            return ebb()
        if self is PassageWindow.NEAP:
            return neap()
