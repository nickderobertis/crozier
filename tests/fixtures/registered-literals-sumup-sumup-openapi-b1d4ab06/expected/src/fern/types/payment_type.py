

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentType(enum.StrEnum):
    """
    Payment type used for the transaction.
    """

    CASH = "CASH"
    POS = "POS"
    ECOM = "ECOM"
    RECURRING = "RECURRING"
    BITCOIN = "BITCOIN"
    BALANCE = "BALANCE"
    MOTO = "MOTO"
    BOLETO = "BOLETO"
    DIRECT_DEBIT = "DIRECT_DEBIT"
    APM = "APM"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        cash: typing.Callable[[], T_Result],
        pos: typing.Callable[[], T_Result],
        ecom: typing.Callable[[], T_Result],
        recurring: typing.Callable[[], T_Result],
        bitcoin: typing.Callable[[], T_Result],
        balance: typing.Callable[[], T_Result],
        moto: typing.Callable[[], T_Result],
        boleto: typing.Callable[[], T_Result],
        direct_debit: typing.Callable[[], T_Result],
        apm: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentType.CASH:
            return cash()
        if self is PaymentType.POS:
            return pos()
        if self is PaymentType.ECOM:
            return ecom()
        if self is PaymentType.RECURRING:
            return recurring()
        if self is PaymentType.BITCOIN:
            return bitcoin()
        if self is PaymentType.BALANCE:
            return balance()
        if self is PaymentType.MOTO:
            return moto()
        if self is PaymentType.BOLETO:
            return boleto()
        if self is PaymentType.DIRECT_DEBIT:
            return direct_debit()
        if self is PaymentType.APM:
            return apm()
        if self is PaymentType.UNKNOWN:
            return unknown()
