

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RefreshTransferStatus(enum.StrEnum):
    WAITING_COUNTERPARTY = "WaitingCounterparty"
    WAITING_CONFIRMATIONS = "WaitingConfirmations"

    def visit(
        self, waiting_counterparty: typing.Callable[[], T_Result], waiting_confirmations: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RefreshTransferStatus.WAITING_COUNTERPARTY:
            return waiting_counterparty()
        if self is RefreshTransferStatus.WAITING_CONFIRMATIONS:
            return waiting_confirmations()
