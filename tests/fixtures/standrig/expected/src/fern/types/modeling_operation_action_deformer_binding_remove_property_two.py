

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerBindingRemovePropertyTwo(enum.StrEnum):
    ROTATION = "rotation"

    def visit(self, rotation: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerBindingRemovePropertyTwo.ROTATION:
            return rotation()
