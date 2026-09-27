

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationTargetRolesItemThree(enum.StrEnum):
    EYE_RIGHT = "eye-right"

    def visit(self, eye_right: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationTargetRolesItemThree.EYE_RIGHT:
            return eye_right()
