

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertMonitorType(enum.StrEnum):
    """
    The type of monitor that triggered the alert
    """

    EVENT = "event"
    DEVICE = "device"

    def visit(self, event: typing.Callable[[], T_Result], device: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertMonitorType.EVENT:
            return event()
        if self is AlertMonitorType.DEVICE:
            return device()
