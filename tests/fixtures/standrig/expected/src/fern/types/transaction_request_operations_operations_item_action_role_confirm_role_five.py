

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFive(enum.StrEnum):
    BROW_RIGHT = "brow-right"

    def visit(self, brow_right: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFive.BROW_RIGHT:
            return brow_right()
