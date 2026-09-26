

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduledMessageType(enum.StrEnum):
    """
    The type of the scheduled message. Either `"stream"` or `"private"`.
    """

    STREAM = "stream"
    PRIVATE = "private"

    def visit(self, stream: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduledMessageType.STREAM:
            return stream()
        if self is ScheduledMessageType.PRIVATE:
            return private()
