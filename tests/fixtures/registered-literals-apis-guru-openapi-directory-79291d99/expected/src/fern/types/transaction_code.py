

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionCode(enum.StrEnum):
    """
    An identifier classifying the transaction type.

    This field is only populated for European institutions. For institutions in the US and Canada, this field is set to `null`.

    `adjustment:` Bank adjustment

    `atm:` Cash deposit or withdrawal via an automated teller machine

    `bank charge:` Charge or fee levied by the institution

    `bill payment`: Payment of a bill

    `cash:` Cash deposit or withdrawal

    `cashback:` Cash withdrawal while making a debit card purchase

    `cheque:` Document ordering the payment of money to another person or organization

    `direct debit:` Automatic withdrawal of funds initiated by a third party at a regular interval

    `interest:` Interest earned or incurred

    `purchase:` Purchase made with a debit or credit card

    `standing order:` Payment instructed by the account holder to a third party at a regular interval

    `transfer:` Transfer of money between accounts
    """

    ADJUSTMENT = "adjustment"
    ATM = "atm"
    BANK_CHARGE = "bank charge"
    BILL_PAYMENT = "bill payment"
    CASH = "cash"
    CASHBACK = "cashback"
    CHEQUE = "cheque"
    DIRECT_DEBIT = "direct debit"
    INTEREST = "interest"
    PURCHASE = "purchase"
    STANDING_ORDER = "standing order"
    TRANSFER = "transfer"

    def visit(
        self,
        adjustment: typing.Callable[[], T_Result],
        atm: typing.Callable[[], T_Result],
        bank_charge: typing.Callable[[], T_Result],
        bill_payment: typing.Callable[[], T_Result],
        cash: typing.Callable[[], T_Result],
        cashback: typing.Callable[[], T_Result],
        cheque: typing.Callable[[], T_Result],
        direct_debit: typing.Callable[[], T_Result],
        interest: typing.Callable[[], T_Result],
        purchase: typing.Callable[[], T_Result],
        standing_order: typing.Callable[[], T_Result],
        transfer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionCode.ADJUSTMENT:
            return adjustment()
        if self is TransactionCode.ATM:
            return atm()
        if self is TransactionCode.BANK_CHARGE:
            return bank_charge()
        if self is TransactionCode.BILL_PAYMENT:
            return bill_payment()
        if self is TransactionCode.CASH:
            return cash()
        if self is TransactionCode.CASHBACK:
            return cashback()
        if self is TransactionCode.CHEQUE:
            return cheque()
        if self is TransactionCode.DIRECT_DEBIT:
            return direct_debit()
        if self is TransactionCode.INTEREST:
            return interest()
        if self is TransactionCode.PURCHASE:
            return purchase()
        if self is TransactionCode.STANDING_ORDER:
            return standing_order()
        if self is TransactionCode.TRANSFER:
            return transfer()
