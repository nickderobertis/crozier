

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerBindingRemovePropertyFive(enum.StrEnum):
    OPACITY = "opacity"

    def visit(self, opacity: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerBindingRemovePropertyFive.OPACITY:
            return opacity()
