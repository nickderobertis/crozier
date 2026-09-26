

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamingEventType(enum.StrEnum):
    EVENT = "event"

    def visit(self, event: typing.Callable[[], T_Result]) -> T_Result:
        if self is StreamingEventType.EVENT:
            return event()
