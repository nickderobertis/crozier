

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxNotificationCategory(enum.StrEnum):
    """
    Category of Notification
    """

    SECURITY = "SECURITY"
    MAINTENANCE = "MAINTENANCE"
    FRAUD = "FRAUD"
    CONSENT = "CONSENT"
    NEW_DATA = "NEW_DATA"

    def visit(
        self,
        security: typing.Callable[[], T_Result],
        maintenance: typing.Callable[[], T_Result],
        fraud: typing.Callable[[], T_Result],
        consent: typing.Callable[[], T_Result],
        new_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxNotificationCategory.SECURITY:
            return security()
        if self is FdxNotificationCategory.MAINTENANCE:
            return maintenance()
        if self is FdxNotificationCategory.FRAUD:
            return fraud()
        if self is FdxNotificationCategory.CONSENT:
            return consent()
        if self is FdxNotificationCategory.NEW_DATA:
            return new_data()
