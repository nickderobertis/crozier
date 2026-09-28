

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeZero(enum.StrEnum):
    LEGACY = "legacy"

    def visit(self, legacy: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeZero.LEGACY:
            return legacy()
