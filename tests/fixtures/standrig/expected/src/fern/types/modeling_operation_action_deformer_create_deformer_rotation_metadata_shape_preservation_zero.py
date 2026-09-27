

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationZero(enum.StrEnum):
    RIGID = "rigid"

    def visit(self, rigid: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationZero.RIGID:
            return rigid()
