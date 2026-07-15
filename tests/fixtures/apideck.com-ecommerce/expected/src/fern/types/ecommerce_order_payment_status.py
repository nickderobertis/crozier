

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EcommerceOrderPaymentStatus(str, enum.Enum):
    """
    Current payment status of the order.
    """

    PENDING = "pending"
    AUTHORIZED = "authorized"
    PAID = "paid"
    PARTIAL = "partial"
    REFUNDED = "refunded"
    VOIDED = "voided"
    UNKNOWN = "unknown"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        authorized: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EcommerceOrderPaymentStatus.PENDING:
            return pending()
        if self is EcommerceOrderPaymentStatus.AUTHORIZED:
            return authorized()
        if self is EcommerceOrderPaymentStatus.PAID:
            return paid()
        if self is EcommerceOrderPaymentStatus.PARTIAL:
            return partial()
        if self is EcommerceOrderPaymentStatus.REFUNDED:
            return refunded()
        if self is EcommerceOrderPaymentStatus.VOIDED:
            return voided()
        if self is EcommerceOrderPaymentStatus.UNKNOWN:
            return unknown()
