

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatedIncomeSourceCategory(enum.StrEnum):
    """
    The income category for a specified income source
    """

    OTHER = "OTHER"
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

    def visit(
        self,
        other: typing.Callable[[], T_Result],
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
    ) -> T_Result:
        if self is UserStatedIncomeSourceCategory.OTHER:
            return other()
        if self is UserStatedIncomeSourceCategory.SALARY:
            return salary()
        if self is UserStatedIncomeSourceCategory.UNEMPLOYMENT:
            return unemployment()
        if self is UserStatedIncomeSourceCategory.CASH:
            return cash()
        if self is UserStatedIncomeSourceCategory.GIG_ECONOMY:
            return gig_economy()
        if self is UserStatedIncomeSourceCategory.RENTAL:
            return rental()
        if self is UserStatedIncomeSourceCategory.CHILD_SUPPORT:
            return child_support()
        if self is UserStatedIncomeSourceCategory.MILITARY:
            return military()
        if self is UserStatedIncomeSourceCategory.RETIREMENT:
            return retirement()
        if self is UserStatedIncomeSourceCategory.LONG_TERM_DISABILITY:
            return long_term_disability()
        if self is UserStatedIncomeSourceCategory.BANK_INTEREST:
            return bank_interest()
