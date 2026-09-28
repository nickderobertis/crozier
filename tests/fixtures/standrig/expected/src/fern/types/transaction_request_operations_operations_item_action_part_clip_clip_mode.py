

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionPartClipClipMode(enum.StrEnum):
    ALPHA = "alpha"

    def visit(self, alpha: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionPartClipClipMode.ALPHA:
            return alpha()
