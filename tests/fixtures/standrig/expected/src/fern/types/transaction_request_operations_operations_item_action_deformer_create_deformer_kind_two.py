

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindTwo(enum.StrEnum):
    WARP = "warp"

    def visit(self, warp: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindTwo.WARP:
            return warp()
