

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationOne(enum.StrEnum):
    RIGID_PLUS_WARP = "rigid-plus-warp"

    def visit(self, rigid_plus_warp: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationOne.RIGID_PLUS_WARP:
            return rigid_plus_warp()
