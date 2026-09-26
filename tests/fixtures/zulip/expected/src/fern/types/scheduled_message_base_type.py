

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduledMessageBaseType(enum.StrEnum):
    """
    The type of the scheduled message. Either `"stream"` or `"private"`.
    """

    STREAM = "stream"
    PRIVATE = "private"

    def visit(self, stream: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduledMessageBaseType.STREAM:
            return stream()
        if self is ScheduledMessageBaseType.PRIVATE:
            return private()
