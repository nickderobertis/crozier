

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemOrderOp(enum.StrEnum):
    REORDER = "reorder"

    def visit(self, reorder: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemOrderOp.REORDER:
            return reorder()
