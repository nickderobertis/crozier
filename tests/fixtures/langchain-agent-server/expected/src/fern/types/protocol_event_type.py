

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProtocolEventType(enum.StrEnum):
    EVENT = "event"

    def visit(self, event: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProtocolEventType.EVENT:
            return event()
