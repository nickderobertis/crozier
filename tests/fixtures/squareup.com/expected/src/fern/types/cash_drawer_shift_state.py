

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CashDrawerShiftState(enum.StrEnum):
    """
    The current state of a cash drawer shift.
    """

    OPEN = "OPEN"
    ENDED = "ENDED"
    CLOSED = "CLOSED"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        ended: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CashDrawerShiftState.OPEN:
            return open()
        if self is CashDrawerShiftState.ENDED:
            return ended()
        if self is CashDrawerShiftState.CLOSED:
            return closed()
