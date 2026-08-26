

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CellNotificationOp(enum.StrEnum):
    CELL_OP = "cell-op"

    def visit(self, cell_op: typing.Callable[[], T_Result]) -> T_Result:
        if self is CellNotificationOp.CELL_OP:
            return cell_op()
