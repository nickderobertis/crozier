

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFour(enum.StrEnum):
    BROW_LEFT = "brow-left"

    def visit(self, brow_left: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFour.BROW_LEFT:
            return brow_left()
