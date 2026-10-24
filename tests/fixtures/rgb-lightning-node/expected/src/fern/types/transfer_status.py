

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferStatus(enum.StrEnum):
    INITIATED = "Initiated"
    WAITING_COUNTERPARTY = "WaitingCounterparty"
    WAITING_SAFE_HEIGHT = "WaitingSafeHeight"
    WAITING_CONFIRMATIONS = "WaitingConfirmations"
    WAITING_BROADCAST = "WaitingBroadcast"
    SETTLED = "Settled"
    FAILED = "Failed"

    def visit(
        self,
        initiated: typing.Callable[[], T_Result],
        waiting_counterparty: typing.Callable[[], T_Result],
        waiting_safe_height: typing.Callable[[], T_Result],
        waiting_confirmations: typing.Callable[[], T_Result],
        waiting_broadcast: typing.Callable[[], T_Result],
        settled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferStatus.INITIATED:
            return initiated()
        if self is TransferStatus.WAITING_COUNTERPARTY:
            return waiting_counterparty()
        if self is TransferStatus.WAITING_SAFE_HEIGHT:
            return waiting_safe_height()
        if self is TransferStatus.WAITING_CONFIRMATIONS:
            return waiting_confirmations()
        if self is TransferStatus.WAITING_BROADCAST:
            return waiting_broadcast()
        if self is TransferStatus.SETTLED:
            return settled()
        if self is TransferStatus.FAILED:
            return failed()
