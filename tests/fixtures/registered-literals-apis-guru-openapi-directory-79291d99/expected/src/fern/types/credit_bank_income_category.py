

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditBankIncomeCategory(enum.StrEnum):
    """
    The income category.
    """

    SALARY = "SALARY"
    UNEMPLOYMENT = "UNEMPLOYMENT"
    CASH = "CASH"
    GIG_ECONOMY = "GIG_ECONOMY"
    RENTAL = "RENTAL"
    CHILD_SUPPORT = "CHILD_SUPPORT"
    MILITARY = "MILITARY"
    RETIREMENT = "RETIREMENT"
    LONG_TERM_DISABILITY = "LONG_TERM_DISABILITY"
    BANK_INTEREST = "BANK_INTEREST"
    CASH_DEPOSIT = "CASH_DEPOSIT"
    TRANSFER_FROM_APPLICATION = "TRANSFER_FROM_APPLICATION"
    TAX_REFUND = "TAX_REFUND"
    OTHER = "OTHER"

    def visit(
        self,
        salary: typing.Callable[[], T_Result],
        unemployment: typing.Callable[[], T_Result],
        cash: typing.Callable[[], T_Result],
        gig_economy: typing.Callable[[], T_Result],
        rental: typing.Callable[[], T_Result],
        child_support: typing.Callable[[], T_Result],
        military: typing.Callable[[], T_Result],
        retirement: typing.Callable[[], T_Result],
        long_term_disability: typing.Callable[[], T_Result],
        bank_interest: typing.Callable[[], T_Result],
        cash_deposit: typing.Callable[[], T_Result],
        transfer_from_application: typing.Callable[[], T_Result],
        tax_refund: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditBankIncomeCategory.SALARY:
            return salary()
        if self is CreditBankIncomeCategory.UNEMPLOYMENT:
            return unemployment()
        if self is CreditBankIncomeCategory.CASH:
            return cash()
        if self is CreditBankIncomeCategory.GIG_ECONOMY:
            return gig_economy()
        if self is CreditBankIncomeCategory.RENTAL:
            return rental()
        if self is CreditBankIncomeCategory.CHILD_SUPPORT:
            return child_support()
        if self is CreditBankIncomeCategory.MILITARY:
            return military()
        if self is CreditBankIncomeCategory.RETIREMENT:
            return retirement()
        if self is CreditBankIncomeCategory.LONG_TERM_DISABILITY:
            return long_term_disability()
        if self is CreditBankIncomeCategory.BANK_INTEREST:
            return bank_interest()
        if self is CreditBankIncomeCategory.CASH_DEPOSIT:
            return cash_deposit()
        if self is CreditBankIncomeCategory.TRANSFER_FROM_APPLICATION:
            return transfer_from_application()
        if self is CreditBankIncomeCategory.TAX_REFUND:
            return tax_refund()
        if self is CreditBankIncomeCategory.OTHER:
            return other()
