

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataAxisOption(enum.StrEnum):
    """
    Allowed values for the render.data_axis option.
    """

    ROW = "row"
    COLUMN = "column"

    def visit(self, row: typing.Callable[[], T_Result], column: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataAxisOption.ROW:
            return row()
        if self is DataAxisOption.COLUMN:
            return column()
