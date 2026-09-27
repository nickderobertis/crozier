

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationTargetRolesItemFour(enum.StrEnum):
    BROW_LEFT = "brow-left"

    def visit(self, brow_left: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationTargetRolesItemFour.BROW_LEFT:
            return brow_left()
