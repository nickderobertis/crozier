

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwelve(enum.StrEnum):
    HAIR_TAIL_RIGHT = "hair-tail-right"

    def visit(self, hair_tail_right: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwelve.HAIR_TAIL_RIGHT:
            return hair_tail_right()
