

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HarvestBoardHarvestsPendingReason(enum.StrEnum):
    LEDGER_CLOSED = "ledger-closed"

    def visit(self, ledger_closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is HarvestBoardHarvestsPendingReason.LEDGER_CLOSED:
            return ledger_closed()
