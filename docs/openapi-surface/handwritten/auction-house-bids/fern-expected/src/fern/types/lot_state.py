

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LotState(enum.StrEnum):
    OPEN = "open"
    CLOSING = "closing"
    SOLD = "sold"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        closing: typing.Callable[[], T_Result],
        sold: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LotState.OPEN:
            return open()
        if self is LotState.CLOSING:
            return closing()
        if self is LotState.SOLD:
            return sold()
