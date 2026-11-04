

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckoutStatus(enum.StrEnum):
    """
    Current high-level state of the checkout. `PENDING` means the checkout exists but is not yet completed, `PAID` means a payment succeeded, `FAILED` means the latest processing attempt failed, and `EXPIRED` means the checkout can no longer be processed.
    """

    PENDING = "PENDING"
    FAILED = "FAILED"
    PAID = "PAID"
    EXPIRED = "EXPIRED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CheckoutStatus.PENDING:
            return pending()
        if self is CheckoutStatus.FAILED:
            return failed()
        if self is CheckoutStatus.PAID:
            return paid()
        if self is CheckoutStatus.EXPIRED:
            return expired()
