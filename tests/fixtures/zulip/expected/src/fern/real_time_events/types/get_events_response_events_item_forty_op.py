

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyOp(enum.StrEnum):
    START = "start"

    def visit(self, start: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyOp.START:
            return start()
