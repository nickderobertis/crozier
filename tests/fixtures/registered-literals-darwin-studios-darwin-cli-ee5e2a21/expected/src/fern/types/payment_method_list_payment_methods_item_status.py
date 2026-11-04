

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentMethodListPaymentMethodsItemStatus(enum.StrEnum):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentMethodListPaymentMethodsItemStatus.ACTIVE:
            return active()
        if self is PaymentMethodListPaymentMethodsItemStatus.EXPIRED:
            return expired()
        if self is PaymentMethodListPaymentMethodsItemStatus.REVOKED:
            return revoked()
