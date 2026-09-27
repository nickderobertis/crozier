

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEleven(enum.StrEnum):
    HAIR_TAIL_LEFT = "hair-tail-left"

    def visit(self, hair_tail_left: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEleven.HAIR_TAIL_LEFT:
            return hair_tail_left()
