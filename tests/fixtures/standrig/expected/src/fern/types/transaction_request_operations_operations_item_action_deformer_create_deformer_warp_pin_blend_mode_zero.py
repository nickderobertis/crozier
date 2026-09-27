

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeZero(enum.StrEnum):
    LEGACY = "legacy"

    def visit(self, legacy: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeZero.LEGACY:
            return legacy()
