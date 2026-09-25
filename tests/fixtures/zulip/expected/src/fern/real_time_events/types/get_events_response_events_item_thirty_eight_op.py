

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemThirtyEightOp(enum.StrEnum):
    START = "start"

    def visit(self, start: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemThirtyEightOp.START:
            return start()
