

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleReclassifyRoleFive(enum.StrEnum):
    BROW_RIGHT = "brow-right"

    def visit(self, brow_right: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleReclassifyRoleFive.BROW_RIGHT:
            return brow_right()
