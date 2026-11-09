

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxNotificationPriority(enum.StrEnum):
    """
    Priority of notification
    """

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def visit(
        self,
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxNotificationPriority.HIGH:
            return high()
        if self is FdxNotificationPriority.MEDIUM:
            return medium()
        if self is FdxNotificationPriority.LOW:
            return low()
