

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertNotificationsItemNotificationType(enum.StrEnum):
    """
    The type of notification
    """

    EMAIL = "email"
    SLACK = "slack"

    def visit(self, email: typing.Callable[[], T_Result], slack: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertNotificationsItemNotificationType.EMAIL:
            return email()
        if self is AlertNotificationsItemNotificationType.SLACK:
            return slack()
