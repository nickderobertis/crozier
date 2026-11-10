

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditBankIncomePayFrequency(enum.StrEnum):
    """
    The income pay frequency.
    """

    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"
    DAILY = "DAILY"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        weekly: typing.Callable[[], T_Result],
        biweekly: typing.Callable[[], T_Result],
        semi_monthly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditBankIncomePayFrequency.WEEKLY:
            return weekly()
        if self is CreditBankIncomePayFrequency.BIWEEKLY:
            return biweekly()
        if self is CreditBankIncomePayFrequency.SEMI_MONTHLY:
            return semi_monthly()
        if self is CreditBankIncomePayFrequency.MONTHLY:
            return monthly()
        if self is CreditBankIncomePayFrequency.DAILY:
            return daily()
        if self is CreditBankIncomePayFrequency.UNKNOWN:
            return unknown()
