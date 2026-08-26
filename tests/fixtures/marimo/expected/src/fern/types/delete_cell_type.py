

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteCellType(enum.StrEnum):
    DELETE_CELL = "delete-cell"

    def visit(self, delete_cell: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteCellType.DELETE_CELL:
            return delete_cell()
