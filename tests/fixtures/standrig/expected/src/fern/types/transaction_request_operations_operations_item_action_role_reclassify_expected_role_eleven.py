

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEleven(enum.StrEnum):
    HAIR_TAIL_LEFT = "hair-tail-left"

    def visit(self, hair_tail_left: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEleven.HAIR_TAIL_LEFT:
            return hair_tail_left()
