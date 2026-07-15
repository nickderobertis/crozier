

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreditNoteAllocationsItemType(str, enum.Enum):
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
        if self is CreditNoteAllocationsItemType.INVOICE:
            return invoice()
        if self is CreditNoteAllocationsItemType.ORDER:
            return order()
        if self is CreditNoteAllocationsItemType.EXPENSE:
            return expense()
        if self is CreditNoteAllocationsItemType.CREDIT_MEMO:
            return credit_memo()
        if self is CreditNoteAllocationsItemType.OVER_PAYMENT:
            return over_payment()
        if self is CreditNoteAllocationsItemType.PRE_PAYMENT:
            return pre_payment()
