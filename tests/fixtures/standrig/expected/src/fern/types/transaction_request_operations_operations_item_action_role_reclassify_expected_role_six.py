

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSix(enum.StrEnum):
    FACE_FEATURE = "face-feature"

    def visit(self, face_feature: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSix.FACE_FEATURE:
            return face_feature()
