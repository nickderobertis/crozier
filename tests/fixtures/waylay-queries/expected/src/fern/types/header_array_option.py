

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HeaderArrayOption(enum.StrEnum):
    """
    Allowed values for the render.header_array option.
    """

    ROW = "row"
    COLUMN = "column"

    def visit(self, row: typing.Callable[[], T_Result], column: typing.Callable[[], T_Result]) -> T_Result:
        if self is HeaderArrayOption.ROW:
            return row()
        if self is HeaderArrayOption.COLUMN:
            return column()
