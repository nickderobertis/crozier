

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExecuteCellsCommandType(enum.StrEnum):
    EXECUTE_CELLS = "execute-cells"

    def visit(self, execute_cells: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExecuteCellsCommandType.EXECUTE_CELLS:
            return execute_cells()
