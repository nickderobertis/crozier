

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleConfirmRoleFourteen(enum.StrEnum):
    TORSO = "torso"

    def visit(self, torso: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleConfirmRoleFourteen.TORSO:
            return torso()
