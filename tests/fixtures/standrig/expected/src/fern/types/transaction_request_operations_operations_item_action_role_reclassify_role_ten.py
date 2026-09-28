

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTen(enum.StrEnum):
    HAIR_SIDE = "hair-side"

    def visit(self, hair_side: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTen.HAIR_SIDE:
            return hair_side()
