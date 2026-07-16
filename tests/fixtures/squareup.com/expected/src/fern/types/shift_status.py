

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShiftStatus(enum.StrEnum):
    """
    Enumerates the possible status of a `Shift`.
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"

    def visit(self, open: typing.Callable[[], T_Result], closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ShiftStatus.OPEN:
            return open()
        if self is ShiftStatus.CLOSED:
            return closed()
