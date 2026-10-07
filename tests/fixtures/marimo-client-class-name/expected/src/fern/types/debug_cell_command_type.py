

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DebugCellCommandType(enum.StrEnum):
    DEBUG_CELL = "debug-cell"

    def visit(self, debug_cell: typing.Callable[[], T_Result]) -> T_Result:
        if self is DebugCellCommandType.DEBUG_CELL:
            return debug_cell()
