

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxNotificationPayloadIdType(enum.StrEnum):
    """
    Type of entity causing origination of a notification
    """

    ACCOUNT = "ACCOUNT"
    CUSTOMER = "CUSTOMER"
    PARTY = "PARTY"
    MAINTENANCE = "MAINTENANCE"
    CONSENT = "CONSENT"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        customer: typing.Callable[[], T_Result],
        party: typing.Callable[[], T_Result],
        maintenance: typing.Callable[[], T_Result],
        consent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxNotificationPayloadIdType.ACCOUNT:
            return account()
        if self is FdxNotificationPayloadIdType.CUSTOMER:
            return customer()
        if self is FdxNotificationPayloadIdType.PARTY:
            return party()
        if self is FdxNotificationPayloadIdType.MAINTENANCE:
            return maintenance()
        if self is FdxNotificationPayloadIdType.CONSENT:
            return consent()
