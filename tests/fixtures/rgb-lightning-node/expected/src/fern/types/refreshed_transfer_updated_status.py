

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RefreshedTransferUpdatedStatus(enum.StrEnum):
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
        if self is RefreshedTransferUpdatedStatus.INITIATED:
            return initiated()
        if self is RefreshedTransferUpdatedStatus.WAITING_COUNTERPARTY:
            return waiting_counterparty()
        if self is RefreshedTransferUpdatedStatus.WAITING_SAFE_HEIGHT:
            return waiting_safe_height()
        if self is RefreshedTransferUpdatedStatus.WAITING_CONFIRMATIONS:
            return waiting_confirmations()
        if self is RefreshedTransferUpdatedStatus.WAITING_BROADCAST:
            return waiting_broadcast()
        if self is RefreshedTransferUpdatedStatus.SETTLED:
            return settled()
        if self is RefreshedTransferUpdatedStatus.FAILED:
            return failed()
