

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceOne(enum.StrEnum):
    NORMALIZED = "normalized"

    def visit(self, normalized: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceOne.NORMALIZED:
            return normalized()
