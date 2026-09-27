

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemTargetRolesItemEight(enum.StrEnum):
    HAIR_FRONT = "hair-front"

    def visit(self, hair_front: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemTargetRolesItemEight.HAIR_FRONT:
            return hair_front()
