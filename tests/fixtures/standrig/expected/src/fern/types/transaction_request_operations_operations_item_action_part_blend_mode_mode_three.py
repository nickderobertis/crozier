

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionPartBlendModeModeThree(enum.StrEnum):
    ADDITIVE = "additive"

    def visit(self, additive: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionPartBlendModeModeThree.ADDITIVE:
            return additive()
