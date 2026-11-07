

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseCountAnalyticsByCaseFiledDateMonthString(enum.StrEnum):
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"

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
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.JANUARY:
            return january()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.FEBRUARY:
            return february()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.MARCH:
            return march()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.APRIL:
            return april()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.MAY:
            return may()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.JUNE:
            return june()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.JULY:
            return july()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.AUGUST:
            return august()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.SEPTEMBER:
            return september()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.OCTOBER:
            return october()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.NOVEMBER:
            return november()
        if self is CaseCountAnalyticsByCaseFiledDateMonthString.DECEMBER:
            return december()
