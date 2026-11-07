

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonitorSourceType(enum.StrEnum):
    """
    The type of source to monitor. Supported values are "event" and "heartbeat".
    """

    EVENT = "event"
    HEARTBEAT = "heartbeat"

    def visit(self, event: typing.Callable[[], T_Result], heartbeat: typing.Callable[[], T_Result]) -> T_Result:
        if self is MonitorSourceType.EVENT:
            return event()
        if self is MonitorSourceType.HEARTBEAT:
            return heartbeat()
