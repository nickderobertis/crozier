

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindZero(enum.StrEnum):
    GROUP = "group"

    def visit(self, group: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindZero.GROUP:
            return group()
