

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RowDataSetDataAxis(enum.StrEnum):
    COLUMN = "column"

    def visit(self, column: typing.Callable[[], T_Result]) -> T_Result:
        if self is RowDataSetDataAxis.COLUMN:
            return column()
