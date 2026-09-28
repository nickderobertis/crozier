

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleReclassifyExpectedRoleThree(enum.StrEnum):
    EYE_RIGHT = "eye-right"

    def visit(self, eye_right: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleReclassifyExpectedRoleThree.EYE_RIGHT:
            return eye_right()
