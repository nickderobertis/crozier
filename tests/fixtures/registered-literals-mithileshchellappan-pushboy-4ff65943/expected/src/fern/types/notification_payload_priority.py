

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationPayloadPriority(enum.StrEnum):
    HIGH = "high"
    NORMAL = "normal"

    def visit(self, high: typing.Callable[[], T_Result], normal: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotificationPayloadPriority.HIGH:
            return high()
        if self is NotificationPayloadPriority.NORMAL:
            return normal()
