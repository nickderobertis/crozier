

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateMonitorSourceType(enum.StrEnum):
    """
    The type of source to monitor. Supported values are "event" and "heartbeat".
    """

    EVENT = "event"
    HEARTBEAT = "heartbeat"

    def visit(self, event: typing.Callable[[], T_Result], heartbeat: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateMonitorSourceType.EVENT:
            return event()
        if self is CreateMonitorSourceType.HEARTBEAT:
            return heartbeat()
