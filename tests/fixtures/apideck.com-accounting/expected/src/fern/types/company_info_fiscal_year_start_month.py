

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CompanyInfoFiscalYearStartMonth(str, enum.Enum):
    """
    The start month of fiscal year.
    """

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
        if self is CompanyInfoFiscalYearStartMonth.JANUARY:
            return january()
        if self is CompanyInfoFiscalYearStartMonth.FEBRUARY:
            return february()
        if self is CompanyInfoFiscalYearStartMonth.MARCH:
            return march()
        if self is CompanyInfoFiscalYearStartMonth.APRIL:
            return april()
        if self is CompanyInfoFiscalYearStartMonth.MAY:
            return may()
        if self is CompanyInfoFiscalYearStartMonth.JUNE:
            return june()
        if self is CompanyInfoFiscalYearStartMonth.JULY:
            return july()
        if self is CompanyInfoFiscalYearStartMonth.AUGUST:
            return august()
        if self is CompanyInfoFiscalYearStartMonth.SEPTEMBER:
            return september()
        if self is CompanyInfoFiscalYearStartMonth.OCTOBER:
            return october()
        if self is CompanyInfoFiscalYearStartMonth.NOVEMBER:
            return november()
        if self is CompanyInfoFiscalYearStartMonth.DECEMBER:
            return december()
