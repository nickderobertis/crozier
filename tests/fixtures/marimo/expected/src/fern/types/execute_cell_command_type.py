

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExecuteCellCommandType(enum.StrEnum):
    EXECUTE_CELL = "execute-cell"

    def visit(self, execute_cell: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExecuteCellCommandType.EXECUTE_CELL:
            return execute_cell()
