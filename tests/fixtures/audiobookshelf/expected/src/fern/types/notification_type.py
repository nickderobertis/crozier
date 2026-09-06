

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationType(enum.StrEnum):
    """
    The notification's type.
    """

    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    FAILURE = "failure"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationType.INFO:
            return info()
        if self is NotificationType.SUCCESS:
            return success()
        if self is NotificationType.WARNING:
            return warning()
        if self is NotificationType.FAILURE:
            return failure()
