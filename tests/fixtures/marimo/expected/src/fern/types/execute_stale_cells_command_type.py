

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExecuteStaleCellsCommandType(enum.StrEnum):
    EXECUTE_STALE_CELLS = "execute-stale-cells"

    def visit(self, execute_stale_cells: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExecuteStaleCellsCommandType.EXECUTE_STALE_CELLS:
            return execute_stale_cells()
