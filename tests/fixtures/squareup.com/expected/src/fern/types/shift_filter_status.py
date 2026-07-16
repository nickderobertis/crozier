

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ShiftFilterStatus(str, enum.Enum):
    """
    Specifies the `status` of `Shift` records to be returned.
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"

    def visit(self, open: typing.Callable[[], T_Result], closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ShiftFilterStatus.OPEN:
            return open()
        if self is ShiftFilterStatus.CLOSED:
            return closed()
