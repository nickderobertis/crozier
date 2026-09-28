

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionZero(enum.StrEnum):
    PARENT_FIRST = "parent-first"

    def visit(self, parent_first: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionZero.PARENT_FIRST:
            return parent_first()
