

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerTargetsSetModeZero(enum.StrEnum):
    REPLACE = "replace"

    def visit(self, replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerTargetsSetModeZero.REPLACE:
            return replace()
