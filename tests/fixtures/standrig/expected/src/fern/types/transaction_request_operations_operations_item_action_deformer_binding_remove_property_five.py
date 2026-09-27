

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFive(enum.StrEnum):
    OPACITY = "opacity"

    def visit(self, opacity: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFive.OPACITY:
            return opacity()
