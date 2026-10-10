

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrossingWindow(enum.StrEnum):
    """
    Scheduled crossings never leave at slack water.
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
        if self is CrossingWindow.SLACK:
            return slack()
        if self is CrossingWindow.FLOOD:
            return flood()
        if self is CrossingWindow.EBB:
            return ebb()
        if self is CrossingWindow.NEAP:
            return neap()
