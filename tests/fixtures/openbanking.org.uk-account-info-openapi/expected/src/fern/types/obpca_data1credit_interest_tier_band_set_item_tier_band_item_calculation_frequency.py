

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency(str, enum.Enum):
    """
    How often is credit interest calculated for the account.
    """

    PER_ACADEMIC_TERM = "PerAcademicTerm"
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
        per_academic_term: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        half_yearly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
        per_statement_date: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        yearly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.PER_ACADEMIC_TERM:
            return per_academic_term()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.DAILY:
            return daily()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.HALF_YEARLY:
            return half_yearly()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.MONTHLY:
            return monthly()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.OTHER:
            return other()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.QUARTERLY:
            return quarterly()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.PER_STATEMENT_DATE:
            return per_statement_date()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.WEEKLY:
            return weekly()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency.YEARLY:
            return yearly()
