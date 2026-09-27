

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerKindSetKindOne(enum.StrEnum):
    ROTATE = "rotate"

    def visit(self, rotate: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerKindSetKindOne.ROTATE:
            return rotate()
