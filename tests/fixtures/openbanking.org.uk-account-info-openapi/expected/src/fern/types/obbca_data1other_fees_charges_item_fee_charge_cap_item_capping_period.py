

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod(enum.StrEnum):
    """
    Period e.g. day, week, month etc. for which the fee/charge is capped
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
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod.DAY:
            return day()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod.HALF_YEAR:
            return half_year()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod.MONTH:
            return month()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod.QUARTER:
            return quarter()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod.WEEK:
            return week()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemCappingPeriod.YEAR:
            return year()
