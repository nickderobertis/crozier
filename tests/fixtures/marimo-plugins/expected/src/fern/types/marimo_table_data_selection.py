

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoTableDataSelection(enum.StrEnum):
    SINGLE = "single"
    MULTI = "multi"
    SINGLE_CELL = "single-cell"
    MULTI_CELL = "multi-cell"

    def visit(
        self,
        single: typing.Callable[[], T_Result],
        multi: typing.Callable[[], T_Result],
        single_cell: typing.Callable[[], T_Result],
        multi_cell: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoTableDataSelection.SINGLE:
            return single()
        if self is MarimoTableDataSelection.MULTI:
            return multi()
        if self is MarimoTableDataSelection.SINGLE_CELL:
            return single_cell()
        if self is MarimoTableDataSelection.MULTI_CELL:
            return multi_cell()
