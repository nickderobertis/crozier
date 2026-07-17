

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod(
    enum.StrEnum
):
    """
    Period e.g. day, week, month etc. for which the fee/charge is capped
    """

    ACADEMIC_TERM = "AcademicTerm"
    DAY = "Day"
    HALF_YEAR = "Half Year"
    MONTH = "Month"
    QUARTER = "Quarter"
    WEEK = "Week"
    YEAR = "Year"

    def visit(
        self,
        academic_term: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        half_year: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        quarter: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.ACADEMIC_TERM
        ):
            return academic_term()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.DAY
        ):
            return day()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.HALF_YEAR
        ):
            return half_year()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.MONTH
        ):
            return month()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.QUARTER
        ):
            return quarter()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.WEEK
        ):
            return week()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.YEAR
        ):
            return year()
