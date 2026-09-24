

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsGroupedRequestAlertStatus(enum.StrEnum):
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
        if self is GetAlertsGroupedRequestAlertStatus.OPEN:
            return open()
        if self is GetAlertsGroupedRequestAlertStatus.DISMISSED:
            return dismissed()
        if self is GetAlertsGroupedRequestAlertStatus.SNOOZED:
            return snoozed()
        if self is GetAlertsGroupedRequestAlertStatus.RESOLVED:
            return resolved()
        if self is GetAlertsGroupedRequestAlertStatus.PENDING_RESOLUTION:
            return pending_resolution()
