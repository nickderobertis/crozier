

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CashDrawerEventType(str, enum.Enum):
    """
    The types of events on a CashDrawerShift.
    Each event type represents an employee action on the actual cash drawer
    represented by a CashDrawerShift.
    """

    NO_SALE = "NO_SALE"
    CASH_TENDER_PAYMENT = "CASH_TENDER_PAYMENT"
    OTHER_TENDER_PAYMENT = "OTHER_TENDER_PAYMENT"
    CASH_TENDER_CANCELLED_PAYMENT = "CASH_TENDER_CANCELLED_PAYMENT"
    OTHER_TENDER_CANCELLED_PAYMENT = "OTHER_TENDER_CANCELLED_PAYMENT"
    CASH_TENDER_REFUND = "CASH_TENDER_REFUND"
    OTHER_TENDER_REFUND = "OTHER_TENDER_REFUND"
    PAID_IN = "PAID_IN"
    PAID_OUT = "PAID_OUT"

    def visit(
        self,
        no_sale: typing.Callable[[], T_Result],
        cash_tender_payment: typing.Callable[[], T_Result],
        other_tender_payment: typing.Callable[[], T_Result],
        cash_tender_cancelled_payment: typing.Callable[[], T_Result],
        other_tender_cancelled_payment: typing.Callable[[], T_Result],
        cash_tender_refund: typing.Callable[[], T_Result],
        other_tender_refund: typing.Callable[[], T_Result],
        paid_in: typing.Callable[[], T_Result],
        paid_out: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CashDrawerEventType.NO_SALE:
            return no_sale()
        if self is CashDrawerEventType.CASH_TENDER_PAYMENT:
            return cash_tender_payment()
        if self is CashDrawerEventType.OTHER_TENDER_PAYMENT:
            return other_tender_payment()
        if self is CashDrawerEventType.CASH_TENDER_CANCELLED_PAYMENT:
            return cash_tender_cancelled_payment()
        if self is CashDrawerEventType.OTHER_TENDER_CANCELLED_PAYMENT:
            return other_tender_cancelled_payment()
        if self is CashDrawerEventType.CASH_TENDER_REFUND:
            return cash_tender_refund()
        if self is CashDrawerEventType.OTHER_TENDER_REFUND:
            return other_tender_refund()
        if self is CashDrawerEventType.PAID_IN:
            return paid_in()
        if self is CashDrawerEventType.PAID_OUT:
            return paid_out()
