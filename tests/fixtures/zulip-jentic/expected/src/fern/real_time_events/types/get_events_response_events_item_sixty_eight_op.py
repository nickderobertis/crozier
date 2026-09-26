

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSixtyEightOp(enum.StrEnum):
    UPDATE = "update"

    def visit(self, update: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSixtyEightOp.UPDATE:
            return update()
