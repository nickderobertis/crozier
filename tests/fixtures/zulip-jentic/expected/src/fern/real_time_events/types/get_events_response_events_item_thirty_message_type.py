

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemThirtyMessageType(enum.StrEnum):
    """
    The type of message. Either `"stream"` or `"private"`.
    """

    PRIVATE = "private"
    STREAM = "stream"

    def visit(self, private: typing.Callable[[], T_Result], stream: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemThirtyMessageType.PRIVATE:
            return private()
        if self is GetEventsResponseEventsItemThirtyMessageType.STREAM:
            return stream()
