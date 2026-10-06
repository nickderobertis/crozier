

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MoveCellType(enum.StrEnum):
    MOVE_CELL = "move-cell"

    def visit(self, move_cell: typing.Callable[[], T_Result]) -> T_Result:
        if self is MoveCellType.MOVE_CELL:
            return move_cell()
