

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemMessageIdOp(enum.StrEnum):
    STOP = "stop"

    def visit(self, stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemMessageIdOp.STOP:
            return stop()
