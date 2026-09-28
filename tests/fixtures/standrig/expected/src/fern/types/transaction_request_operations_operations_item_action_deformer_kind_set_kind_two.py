

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerKindSetKindTwo(enum.StrEnum):
    WARP = "warp"

    def visit(self, warp: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerKindSetKindTwo.WARP:
            return warp()
