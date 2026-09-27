

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThree(enum.StrEnum):
    EYE_RIGHT = "eye-right"

    def visit(self, eye_right: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThree.EYE_RIGHT:
            return eye_right()
