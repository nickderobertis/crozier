

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemTargetRolesItemOne(enum.StrEnum):
    FACE = "face"

    def visit(self, face: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemTargetRolesItemOne.FACE:
            return face()
