

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod(str, enum.Enum):
    """
    Specifies the period of a fixed length overdraft agreement
    """

    DAY = "Day"
    HALF_YEAR = "Half Year"
    MONTH = "Month"
    QUARTER = "Quarter"
    WEEK = "Week"
    YEAR = "Year"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        half_year: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        quarter: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.DAY:
            return day()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.HALF_YEAR:
            return half_year()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.MONTH:
            return month()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.QUARTER:
            return quarter()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.WEEK:
            return week()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.YEAR:
            return year()
