

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod(
    str, enum.Enum
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
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.ACADEMIC_TERM
        ):
            return academic_term()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.DAY
        ):
            return day()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.HALF_YEAR
        ):
            return half_year()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.MONTH
        ):
            return month()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.QUARTER
        ):
            return quarter()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.WEEK
        ):
            return week()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod.YEAR
        ):
            return year()
