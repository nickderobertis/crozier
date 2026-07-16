

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1ProductDetailsFeeFreeLengthPeriod(enum.StrEnum):
    """
    The unit of period (days, weeks, months etc.) of the promotional length
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
        if self is ObbcaData1ProductDetailsFeeFreeLengthPeriod.DAY:
            return day()
        if self is ObbcaData1ProductDetailsFeeFreeLengthPeriod.HALF_YEAR:
            return half_year()
        if self is ObbcaData1ProductDetailsFeeFreeLengthPeriod.MONTH:
            return month()
        if self is ObbcaData1ProductDetailsFeeFreeLengthPeriod.QUARTER:
            return quarter()
        if self is ObbcaData1ProductDetailsFeeFreeLengthPeriod.WEEK:
            return week()
        if self is ObbcaData1ProductDetailsFeeFreeLengthPeriod.YEAR:
            return year()
