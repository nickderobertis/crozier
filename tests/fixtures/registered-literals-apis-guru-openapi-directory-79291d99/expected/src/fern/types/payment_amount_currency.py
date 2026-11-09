

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentAmountCurrency(enum.StrEnum):
    """
    The ISO-4217 currency code of the payment. For standing orders and payment consents, `"GBP"` must be used.
    """

    GBP = "GBP"
    EUR = "EUR"
    PLN = "PLN"
    SEK = "SEK"
    DKK = "DKK"
    NOK = "NOK"

    def visit(
        self,
        gbp: typing.Callable[[], T_Result],
        eur: typing.Callable[[], T_Result],
        pln: typing.Callable[[], T_Result],
        sek: typing.Callable[[], T_Result],
        dkk: typing.Callable[[], T_Result],
        nok: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentAmountCurrency.GBP:
            return gbp()
        if self is PaymentAmountCurrency.EUR:
            return eur()
        if self is PaymentAmountCurrency.PLN:
            return pln()
        if self is PaymentAmountCurrency.SEK:
            return sek()
        if self is PaymentAmountCurrency.DKK:
            return dkk()
        if self is PaymentAmountCurrency.NOK:
            return nok()
