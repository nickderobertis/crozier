

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleReclassifyExpectedRoleTwo(enum.StrEnum):
    EYE_LEFT = "eye-left"

    def visit(self, eye_left: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleReclassifyExpectedRoleTwo.EYE_LEFT:
            return eye_left()
