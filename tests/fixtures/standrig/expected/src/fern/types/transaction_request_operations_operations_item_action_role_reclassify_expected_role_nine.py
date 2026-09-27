

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleNine(enum.StrEnum):
    HAIR_BACK = "hair-back"

    def visit(self, hair_back: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleNine.HAIR_BACK:
            return hair_back()
