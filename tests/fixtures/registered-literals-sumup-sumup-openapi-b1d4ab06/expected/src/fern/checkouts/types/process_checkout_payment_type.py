

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProcessCheckoutPaymentType(enum.StrEnum):
    """
    Payment method used for this processing attempt. It determines which additional request fields are required.
    """

    CARD = "card"
    BOLETO = "boleto"
    IDEAL = "ideal"
    BLIK = "blik"
    BANCONTACT = "bancontact"
    GOOGLE_PAY = "google_pay"
    APPLE_PAY = "apple_pay"

    def visit(
        self,
        card: typing.Callable[[], T_Result],
        boleto: typing.Callable[[], T_Result],
        ideal: typing.Callable[[], T_Result],
        blik: typing.Callable[[], T_Result],
        bancontact: typing.Callable[[], T_Result],
        google_pay: typing.Callable[[], T_Result],
        apple_pay: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProcessCheckoutPaymentType.CARD:
            return card()
        if self is ProcessCheckoutPaymentType.BOLETO:
            return boleto()
        if self is ProcessCheckoutPaymentType.IDEAL:
            return ideal()
        if self is ProcessCheckoutPaymentType.BLIK:
            return blik()
        if self is ProcessCheckoutPaymentType.BANCONTACT:
            return bancontact()
        if self is ProcessCheckoutPaymentType.GOOGLE_PAY:
            return google_pay()
        if self is ProcessCheckoutPaymentType.APPLE_PAY:
            return apple_pay()
