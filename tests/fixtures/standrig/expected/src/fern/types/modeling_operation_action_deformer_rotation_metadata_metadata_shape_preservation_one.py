

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationOne(enum.StrEnum):
    RIGID_PLUS_WARP = "rigid-plus-warp"

    def visit(self, rigid_plus_warp: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationOne.RIGID_PLUS_WARP:
            return rigid_plus_warp()
