

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerKindSetKindOne(enum.StrEnum):
    ROTATE = "rotate"

    def visit(self, rotate: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerKindSetKindOne.ROTATE:
            return rotate()
