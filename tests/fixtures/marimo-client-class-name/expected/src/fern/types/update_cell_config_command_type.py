

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateCellConfigCommandType(enum.StrEnum):
    UPDATE_CELL_CONFIG = "update-cell-config"

    def visit(self, update_cell_config: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateCellConfigCommandType.UPDATE_CELL_CONFIG:
            return update_cell_config()
