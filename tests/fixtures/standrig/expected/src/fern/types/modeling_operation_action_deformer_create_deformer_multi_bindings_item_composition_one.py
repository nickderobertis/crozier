

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionOne(enum.StrEnum):
    LEGACY_ADDITIVE = "legacy-additive"

    def visit(self, legacy_additive: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionOne.LEGACY_ADDITIVE:
            return legacy_additive()
