

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemTargetRolesItemZero(enum.StrEnum):
    UNKNOWN = "unknown"

    def visit(self, unknown: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemTargetRolesItemZero.UNKNOWN:
            return unknown()
