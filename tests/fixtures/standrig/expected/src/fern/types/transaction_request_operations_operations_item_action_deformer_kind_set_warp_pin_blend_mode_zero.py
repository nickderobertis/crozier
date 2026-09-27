

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeZero(enum.StrEnum):
    LEGACY = "legacy"

    def visit(self, legacy: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeZero.LEGACY:
            return legacy()
