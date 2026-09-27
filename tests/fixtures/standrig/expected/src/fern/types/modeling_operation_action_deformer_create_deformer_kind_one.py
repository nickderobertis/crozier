

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerKindOne(enum.StrEnum):
    ROTATE = "rotate"

    def visit(self, rotate: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerKindOne.ROTATE:
            return rotate()
