

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxNotificationSeverity(enum.StrEnum):
    """
    Severity level of notification
    """

    EMERGENCY = "EMERGENCY"
    ALERT = "ALERT"
    WARNING = "WARNING"
    NOTICE = "NOTICE"
    INFO = "INFO"

    def visit(
        self,
        emergency: typing.Callable[[], T_Result],
        alert: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        notice: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxNotificationSeverity.EMERGENCY:
            return emergency()
        if self is FdxNotificationSeverity.ALERT:
            return alert()
        if self is FdxNotificationSeverity.WARNING:
            return warning()
        if self is FdxNotificationSeverity.NOTICE:
            return notice()
        if self is FdxNotificationSeverity.INFO:
            return info()
