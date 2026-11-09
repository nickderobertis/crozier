

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentChannel(enum.StrEnum):
    """
    The channel used to make a payment.
    `online:` transactions that took place online.

    `in store:` transactions that were made at a physical location.

    `other:` transactions that relate to banks, e.g. fees or deposits.
    """

    ONLINE = "online"
    IN_STORE = "in store"
    OTHER = "other"

    def visit(
        self,
        online: typing.Callable[[], T_Result],
        in_store: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentChannel.ONLINE:
            return online()
        if self is PaymentChannel.IN_STORE:
            return in_store()
        if self is PaymentChannel.OTHER:
            return other()
