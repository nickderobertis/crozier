

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyTwoOp(enum.StrEnum):
    ADD = "add"

    def visit(self, add: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyTwoOp.ADD:
            return add()
