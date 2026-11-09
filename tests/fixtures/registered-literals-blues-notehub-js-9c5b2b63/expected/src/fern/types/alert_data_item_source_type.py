

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertDataItemSourceType(enum.StrEnum):
    """
    The type of source.
    """

    EVENT = "event"
    DEVICE = "device"

    def visit(self, event: typing.Callable[[], T_Result], device: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertDataItemSourceType.EVENT:
            return event()
        if self is AlertDataItemSourceType.DEVICE:
            return device()
