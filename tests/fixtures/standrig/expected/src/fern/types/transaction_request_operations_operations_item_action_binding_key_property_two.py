

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionBindingKeyPropertyTwo(enum.StrEnum):
    ROTATION = "rotation"

    def visit(self, rotation: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionBindingKeyPropertyTwo.ROTATION:
            return rotation()
