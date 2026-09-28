

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleReclassifyRoleFourteen(enum.StrEnum):
    TORSO = "torso"

    def visit(self, torso: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleReclassifyRoleFourteen.TORSO:
            return torso()
