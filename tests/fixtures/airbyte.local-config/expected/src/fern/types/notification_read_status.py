

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationReadStatus(enum.StrEnum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(self, succeeded: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotificationReadStatus.SUCCEEDED:
            return succeeded()
        if self is NotificationReadStatus.FAILED:
            return failed()
