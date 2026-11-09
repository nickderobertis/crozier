

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignalPaymentMethod(enum.StrEnum):
    """
    The payment method to complete the transaction after the risk assessment. It may be different from the default payment method.

    `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day

    `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors

    `STANDARD_ACH`: standard ACH by NACHA

    `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow

    `DEBIT_CARD`: if the default payment is over debit card networks

    `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods

    Possible values: `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`
    """

    SAME_DAY_ACH = "SAME_DAY_ACH"
    NEXT_DAY_ACH = "NEXT_DAY_ACH"
    STANDARD_ACH = "STANDARD_ACH"
    REAL_TIME_PAYMENTS = "REAL_TIME_PAYMENTS"
    DEBIT_CARD = "DEBIT_CARD"
    MULTIPLE_PAYMENT_METHODS = "MULTIPLE_PAYMENT_METHODS"

    def visit(
        self,
        same_day_ach: typing.Callable[[], T_Result],
        next_day_ach: typing.Callable[[], T_Result],
        standard_ach: typing.Callable[[], T_Result],
        real_time_payments: typing.Callable[[], T_Result],
        debit_card: typing.Callable[[], T_Result],
        multiple_payment_methods: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SignalPaymentMethod.SAME_DAY_ACH:
            return same_day_ach()
        if self is SignalPaymentMethod.NEXT_DAY_ACH:
            return next_day_ach()
        if self is SignalPaymentMethod.STANDARD_ACH:
            return standard_ach()
        if self is SignalPaymentMethod.REAL_TIME_PAYMENTS:
            return real_time_payments()
        if self is SignalPaymentMethod.DEBIT_CARD:
            return debit_card()
        if self is SignalPaymentMethod.MULTIPLE_PAYMENT_METHODS:
            return multiple_payment_methods()
