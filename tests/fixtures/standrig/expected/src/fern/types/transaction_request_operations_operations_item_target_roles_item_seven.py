

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemTargetRolesItemSeven(enum.StrEnum):
    MOUTH = "mouth"

    def visit(self, mouth: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemTargetRolesItemSeven.MOUTH:
            return mouth()
