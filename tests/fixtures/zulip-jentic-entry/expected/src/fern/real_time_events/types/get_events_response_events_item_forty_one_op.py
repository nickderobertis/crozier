

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyOneOp(enum.StrEnum):
    ADD = "add"

    def visit(self, add: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyOneOp.ADD:
            return add()
