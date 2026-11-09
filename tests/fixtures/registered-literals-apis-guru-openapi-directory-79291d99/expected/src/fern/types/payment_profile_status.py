

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentProfileStatus(enum.StrEnum):
    """
    The status of the given Payment Profile.

    `READY`: This Payment Profile is ready to be used to create transfers using `/transfer/authorization/create` and `/transfer/create`.

    `PENDING`: This Payment Profile is not ready to be used. You’ll need to call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field to initiate the account linking experience.

    `REMOVED`: This Payment Profile has been removed.
    """

    PENDING = "PENDING"
    READY = "READY"
    REMOVED = "REMOVED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentProfileStatus.PENDING:
            return pending()
        if self is PaymentProfileStatus.READY:
            return ready()
        if self is PaymentProfileStatus.REMOVED:
            return removed()
