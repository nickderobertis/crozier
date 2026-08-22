

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NewFilterResponseKind(enum.StrEnum):
    LOGS = "Logs"
    NEW_BLOCKS = "NewBlocks"
    NEW_PENDING_TRANSACTIONS = "NewPendingTransactions"

    def visit(
        self,
        logs: typing.Callable[[], T_Result],
        new_blocks: typing.Callable[[], T_Result],
        new_pending_transactions: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NewFilterResponseKind.LOGS:
            return logs()
        if self is NewFilterResponseKind.NEW_BLOCKS:
            return new_blocks()
        if self is NewFilterResponseKind.NEW_PENDING_TRANSACTIONS:
            return new_pending_transactions()
