

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferRecurringStatus(enum.StrEnum):
    """
    The status of the recurring transfer.

    `active`: The recurring transfer is currently active.
    `cancelled`: The recurring transfer was cancelled by the client or Plaid.
    `expired`: The recurring transfer has completed all originations according to its recurring schedule.
    """

    ACTIVE = "active"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferRecurringStatus.ACTIVE:
            return active()
        if self is TransferRecurringStatus.CANCELLED:
            return cancelled()
        if self is TransferRecurringStatus.EXPIRED:
            return expired()
