

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HistoryModelStatus(enum.StrEnum):
    """
    Status
    """

    OPEN = "OPEN"
    DISMISSED = "DISMISSED"
    SNOOZED = "SNOOZED"
    PENDING_RESOLUTION = "PENDING_RESOLUTION"
    RESOLVED = "RESOLVED"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        dismissed: typing.Callable[[], T_Result],
        snoozed: typing.Callable[[], T_Result],
        pending_resolution: typing.Callable[[], T_Result],
        resolved: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HistoryModelStatus.OPEN:
            return open()
        if self is HistoryModelStatus.DISMISSED:
            return dismissed()
        if self is HistoryModelStatus.SNOOZED:
            return snoozed()
        if self is HistoryModelStatus.PENDING_RESOLUTION:
            return pending_resolution()
        if self is HistoryModelStatus.RESOLVED:
            return resolved()
