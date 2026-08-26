

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCellType(enum.StrEnum):
    CREATE_CELL = "create-cell"

    def visit(self, create_cell: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateCellType.CREATE_CELL:
            return create_cell()
