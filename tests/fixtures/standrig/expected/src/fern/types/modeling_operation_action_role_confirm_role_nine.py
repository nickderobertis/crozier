

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleConfirmRoleNine(enum.StrEnum):
    HAIR_BACK = "hair-back"

    def visit(self, hair_back: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleConfirmRoleNine.HAIR_BACK:
            return hair_back()
