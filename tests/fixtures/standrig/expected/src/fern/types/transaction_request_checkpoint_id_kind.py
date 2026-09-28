

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestCheckpointIdKind(enum.StrEnum):
    RESTORE = "restore"

    def visit(self, restore: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestCheckpointIdKind.RESTORE:
            return restore()
