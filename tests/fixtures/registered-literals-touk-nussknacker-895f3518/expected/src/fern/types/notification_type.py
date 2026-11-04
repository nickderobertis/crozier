

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationType(enum.StrEnum):
    INFO = "info"
    SUCCESS = "success"
    ERROR = "error"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationType.INFO:
            return info()
        if self is NotificationType.SUCCESS:
            return success()
        if self is NotificationType.ERROR:
            return error()
