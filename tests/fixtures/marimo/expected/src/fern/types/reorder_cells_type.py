

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReorderCellsType(enum.StrEnum):
    REORDER_CELLS = "reorder-cells"

    def visit(self, reorder_cells: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReorderCellsType.REORDER_CELLS:
            return reorder_cells()
