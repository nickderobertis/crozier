

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEight(enum.StrEnum):
    HAIR_FRONT = "hair-front"

    def visit(self, hair_front: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEight.HAIR_FRONT:
            return hair_front()
