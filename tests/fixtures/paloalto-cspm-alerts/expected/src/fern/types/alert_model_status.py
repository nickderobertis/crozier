

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertModelStatus(enum.StrEnum):
    """
    Status
    """

    OPEN = "open"
    DISMISSED = "dismissed"
    SNOOZED = "snoozed"
    RESOLVED = "resolved"
    PENDING_RESOLUTION = "pending_resolution"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        dismissed: typing.Callable[[], T_Result],
        snoozed: typing.Callable[[], T_Result],
        resolved: typing.Callable[[], T_Result],
        pending_resolution: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlertModelStatus.OPEN:
            return open()
        if self is AlertModelStatus.DISMISSED:
            return dismissed()
        if self is AlertModelStatus.SNOOZED:
            return snoozed()
        if self is AlertModelStatus.RESOLVED:
            return resolved()
        if self is AlertModelStatus.PENDING_RESOLUTION:
            return pending_resolution()
