

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BerthStatusState(enum.StrEnum):
    FREE = "free"
    OCCUPIED = "occupied"
    CLOSED = "closed"

    def visit(
        self,
        free: typing.Callable[[], T_Result],
        occupied: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BerthStatusState.FREE:
            return free()
        if self is BerthStatusState.OCCUPIED:
            return occupied()
        if self is BerthStatusState.CLOSED:
            return closed()
