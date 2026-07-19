

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LettaStopReasonMessageType(enum.StrEnum):
    """
    The type of the message.
    """

    STOP_REASON = "stop_reason"

    def visit(self, stop_reason: typing.Callable[[], T_Result]) -> T_Result:
        if self is LettaStopReasonMessageType.STOP_REASON:
            return stop_reason()
