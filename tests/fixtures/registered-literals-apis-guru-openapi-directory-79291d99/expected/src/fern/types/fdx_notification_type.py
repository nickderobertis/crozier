

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxNotificationType(enum.StrEnum):
    """
    Type of Notification
    """

    CONSENT_REVOKED = "CONSENT_REVOKED"
    CONSENT_UPDATED = "CONSENT_UPDATED"
    CUSTOM = "CUSTOM"
    SERVICE = "SERVICE"
    BALANCE = "BALANCE"
    PLANNED_OUTAGE = "PLANNED_OUTAGE"

    def visit(
        self,
        consent_revoked: typing.Callable[[], T_Result],
        consent_updated: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
        balance: typing.Callable[[], T_Result],
        planned_outage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxNotificationType.CONSENT_REVOKED:
            return consent_revoked()
        if self is FdxNotificationType.CONSENT_UPDATED:
            return consent_updated()
        if self is FdxNotificationType.CUSTOM:
            return custom()
        if self is FdxNotificationType.SERVICE:
            return service()
        if self is FdxNotificationType.BALANCE:
            return balance()
        if self is FdxNotificationType.PLANNED_OUTAGE:
            return planned_outage()
