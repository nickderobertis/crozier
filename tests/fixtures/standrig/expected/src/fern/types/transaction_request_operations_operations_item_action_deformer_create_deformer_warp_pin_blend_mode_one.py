

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeOne(enum.StrEnum):
    NORMALIZED = "normalized"

    def visit(self, normalized: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeOne.NORMALIZED:
            return normalized()
