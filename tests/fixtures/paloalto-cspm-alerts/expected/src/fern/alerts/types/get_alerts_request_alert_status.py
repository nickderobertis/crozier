

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsRequestAlertStatus(enum.StrEnum):
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
        if self is GetAlertsRequestAlertStatus.OPEN:
            return open()
        if self is GetAlertsRequestAlertStatus.DISMISSED:
            return dismissed()
        if self is GetAlertsRequestAlertStatus.SNOOZED:
            return snoozed()
        if self is GetAlertsRequestAlertStatus.RESOLVED:
            return resolved()
        if self is GetAlertsRequestAlertStatus.PENDING_RESOLUTION:
            return pending_resolution()
