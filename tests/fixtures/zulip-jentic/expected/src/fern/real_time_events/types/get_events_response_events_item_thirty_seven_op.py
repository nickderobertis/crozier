

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemThirtySevenOp(enum.StrEnum):
    START = "start"

    def visit(self, start: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemThirtySevenOp.START:
            return start()
