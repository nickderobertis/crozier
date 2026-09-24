

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DoorsStateBaseOpeningItemState(enum.StrEnum):
    OPEN = "Open"
    CLOSED = "Closed"

    def visit(self, open: typing.Callable[[], T_Result], closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is DoorsStateBaseOpeningItemState.OPEN:
            return open()
        if self is DoorsStateBaseOpeningItemState.CLOSED:
            return closed()
