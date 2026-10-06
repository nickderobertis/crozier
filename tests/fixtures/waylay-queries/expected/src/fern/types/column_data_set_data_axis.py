

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ColumnDataSetDataAxis(enum.StrEnum):
    ROW = "row"

    def visit(self, row: typing.Callable[[], T_Result]) -> T_Result:
        if self is ColumnDataSetDataAxis.ROW:
            return row()
