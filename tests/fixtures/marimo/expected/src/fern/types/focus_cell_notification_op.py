

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FocusCellNotificationOp(enum.StrEnum):
    FOCUS_CELL = "focus-cell"

    def visit(self, focus_cell: typing.Callable[[], T_Result]) -> T_Result:
        if self is FocusCellNotificationOp.FOCUS_CELL:
            return focus_cell()
