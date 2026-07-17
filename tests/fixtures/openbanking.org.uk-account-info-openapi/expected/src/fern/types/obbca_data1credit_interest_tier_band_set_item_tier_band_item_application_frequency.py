

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency(enum.StrEnum):
    """
    How often is interest applied to the BCA for this tier/band i.e. how often the financial institution pays accumulated interest to the customer's BCA.
    """

    DAILY = "Daily"
    HALF_YEARLY = "HalfYearly"
    MONTHLY = "Monthly"
    OTHER = "Other"
    QUARTERLY = "Quarterly"
    PER_STATEMENT_DATE = "PerStatementDate"
    WEEKLY = "Weekly"
    YEARLY = "Yearly"

    def visit(
        self,
        daily: typing.Callable[[], T_Result],
        half_yearly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
        per_statement_date: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        yearly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.DAILY:
            return daily()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.HALF_YEARLY:
            return half_yearly()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.MONTHLY:
            return monthly()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.OTHER:
            return other()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.QUARTERLY:
            return quarterly()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.PER_STATEMENT_DATE:
            return per_statement_date()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.WEEKLY:
            return weekly()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency.YEARLY:
            return yearly()
