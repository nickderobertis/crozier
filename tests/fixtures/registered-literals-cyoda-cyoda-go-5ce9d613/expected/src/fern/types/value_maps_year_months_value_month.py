

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValueMapsYearMonthsValueMonth(enum.StrEnum):
    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"

    def visit(
        self,
        january: typing.Callable[[], T_Result],
        february: typing.Callable[[], T_Result],
        march: typing.Callable[[], T_Result],
        april: typing.Callable[[], T_Result],
        may: typing.Callable[[], T_Result],
        june: typing.Callable[[], T_Result],
        july: typing.Callable[[], T_Result],
        august: typing.Callable[[], T_Result],
        september: typing.Callable[[], T_Result],
        october: typing.Callable[[], T_Result],
        november: typing.Callable[[], T_Result],
        december: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValueMapsYearMonthsValueMonth.JANUARY:
            return january()
        if self is ValueMapsYearMonthsValueMonth.FEBRUARY:
            return february()
        if self is ValueMapsYearMonthsValueMonth.MARCH:
            return march()
        if self is ValueMapsYearMonthsValueMonth.APRIL:
            return april()
        if self is ValueMapsYearMonthsValueMonth.MAY:
            return may()
        if self is ValueMapsYearMonthsValueMonth.JUNE:
            return june()
        if self is ValueMapsYearMonthsValueMonth.JULY:
            return july()
        if self is ValueMapsYearMonthsValueMonth.AUGUST:
            return august()
        if self is ValueMapsYearMonthsValueMonth.SEPTEMBER:
            return september()
        if self is ValueMapsYearMonthsValueMonth.OCTOBER:
            return october()
        if self is ValueMapsYearMonthsValueMonth.NOVEMBER:
            return november()
        if self is ValueMapsYearMonthsValueMonth.DECEMBER:
            return december()
