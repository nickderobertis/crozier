

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleUnit(enum.StrEnum):
    DEG = "deg"

    def visit(self, deg: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleUnit.DEG:
            return deg()
