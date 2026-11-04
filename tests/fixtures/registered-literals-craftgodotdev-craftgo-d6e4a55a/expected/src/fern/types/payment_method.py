

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentMethod(enum.StrEnum):
    CARD = "card"
    BANK = "bank"
    WALLET = "wallet"
    INVOICE = "invoice"

    def visit(
        self,
        card: typing.Callable[[], T_Result],
        bank: typing.Callable[[], T_Result],
        wallet: typing.Callable[[], T_Result],
        invoice: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentMethod.CARD:
            return card()
        if self is PaymentMethod.BANK:
            return bank()
        if self is PaymentMethod.WALLET:
            return wallet()
        if self is PaymentMethod.INVOICE:
            return invoice()
