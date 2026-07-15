

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PaymentAllocationsItemType(str, enum.Enum):
    """
    Type of entity this payment should be attributed to.
    """

    INVOICE = "invoice"
    ORDER = "order"
    EXPENSE = "expense"
    CREDIT_MEMO = "credit_memo"
    OVER_PAYMENT = "over_payment"
    PRE_PAYMENT = "pre_payment"

    def visit(
        self,
        invoice: typing.Callable[[], T_Result],
        order: typing.Callable[[], T_Result],
        expense: typing.Callable[[], T_Result],
        credit_memo: typing.Callable[[], T_Result],
        over_payment: typing.Callable[[], T_Result],
        pre_payment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentAllocationsItemType.INVOICE:
            return invoice()
        if self is PaymentAllocationsItemType.ORDER:
            return order()
        if self is PaymentAllocationsItemType.EXPENSE:
            return expense()
        if self is PaymentAllocationsItemType.CREDIT_MEMO:
            return credit_memo()
        if self is PaymentAllocationsItemType.OVER_PAYMENT:
            return over_payment()
        if self is PaymentAllocationsItemType.PRE_PAYMENT:
            return pre_payment()
