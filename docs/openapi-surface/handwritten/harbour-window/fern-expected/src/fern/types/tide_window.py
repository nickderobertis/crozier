

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TideWindow(enum.StrEnum):
    """
    Tidal window a sailing departs in.
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
        if self is TideWindow.SLACK:
            return slack()
        if self is TideWindow.FLOOD:
            return flood()
        if self is TideWindow.EBB:
            return ebb()
        if self is TideWindow.NEAP:
            return neap()
