

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFiftyEightOp(enum.StrEnum):
    CHANGE = "change"

    def visit(self, change: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFiftyEightOp.CHANGE:
            return change()
