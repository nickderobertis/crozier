

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemMessageDetailsMessageDetailsValueType(enum.StrEnum):
    """
    The type of this message. Either `"stream"` or `"private"`.
    """

    PRIVATE = "private"
    STREAM = "stream"

    def visit(self, private: typing.Callable[[], T_Result], stream: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemMessageDetailsMessageDetailsValueType.PRIVATE:
            return private()
        if self is GetEventsResponseEventsItemMessageDetailsMessageDetailsValueType.STREAM:
            return stream()
