

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionFullSimplePaymentType(enum.StrEnum):
    """
    Simple name of the payment type.
    """

    CASH = "CASH"
    CC_SIGNATURE = "CC_SIGNATURE"
    ELV = "ELV"
    ELV_WITHOUT_SIGNATURE = "ELV_WITHOUT_SIGNATURE"
    CC_CUSTOMER_ENTERED = "CC_CUSTOMER_ENTERED"
    MANUAL_ENTRY = "MANUAL_ENTRY"
    EMV = "EMV"
    RECURRING = "RECURRING"
    BALANCE = "BALANCE"
    MOTO = "MOTO"
    BOLETO = "BOLETO"
    APM = "APM"
    BITCOIN = "BITCOIN"
    CARD = "CARD"

    def visit(
        self,
        cash: typing.Callable[[], T_Result],
        cc_signature: typing.Callable[[], T_Result],
        elv: typing.Callable[[], T_Result],
        elv_without_signature: typing.Callable[[], T_Result],
        cc_customer_entered: typing.Callable[[], T_Result],
        manual_entry: typing.Callable[[], T_Result],
        emv: typing.Callable[[], T_Result],
        recurring: typing.Callable[[], T_Result],
        balance: typing.Callable[[], T_Result],
        moto: typing.Callable[[], T_Result],
        boleto: typing.Callable[[], T_Result],
        apm: typing.Callable[[], T_Result],
        bitcoin: typing.Callable[[], T_Result],
        card: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionFullSimplePaymentType.CASH:
            return cash()
        if self is TransactionFullSimplePaymentType.CC_SIGNATURE:
            return cc_signature()
        if self is TransactionFullSimplePaymentType.ELV:
            return elv()
        if self is TransactionFullSimplePaymentType.ELV_WITHOUT_SIGNATURE:
            return elv_without_signature()
        if self is TransactionFullSimplePaymentType.CC_CUSTOMER_ENTERED:
            return cc_customer_entered()
        if self is TransactionFullSimplePaymentType.MANUAL_ENTRY:
            return manual_entry()
        if self is TransactionFullSimplePaymentType.EMV:
            return emv()
        if self is TransactionFullSimplePaymentType.RECURRING:
            return recurring()
        if self is TransactionFullSimplePaymentType.BALANCE:
            return balance()
        if self is TransactionFullSimplePaymentType.MOTO:
            return moto()
        if self is TransactionFullSimplePaymentType.BOLETO:
            return boleto()
        if self is TransactionFullSimplePaymentType.APM:
            return apm()
        if self is TransactionFullSimplePaymentType.BITCOIN:
            return bitcoin()
        if self is TransactionFullSimplePaymentType.CARD:
            return card()
