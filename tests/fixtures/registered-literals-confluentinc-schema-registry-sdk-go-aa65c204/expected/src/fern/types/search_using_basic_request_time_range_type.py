

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchUsingBasicRequestTimeRangeType(enum.StrEnum):
    CUSTOM = "CUSTOM"
    LAST7DAYS = "LAST_7_DAYS"
    LAST30DAYS = "LAST_30_DAYS"
    LAST_MONTH = "LAST_MONTH"
    THIS_MONTH = "THIS_MONTH"
    TODAY = "TODAY"
    YESTERDAY = "YESTERDAY"
    THIS_YEAR = "THIS_YEAR"
    LAST_YEAR = "LAST_YEAR"
    THIS_QUARTER = "THIS_QUARTER"
    LAST_QUARTER = "LAST_QUARTER"
    LAST3MONTHS = "LAST_3_MONTHS"
    LAST6MONTHS = "LAST_6_MONTHS"
    LAST12MONTHS = "LAST_12_MONTHS"

    def visit(
        self,
        custom: typing.Callable[[], T_Result],
        last7days: typing.Callable[[], T_Result],
        last30days: typing.Callable[[], T_Result],
        last_month: typing.Callable[[], T_Result],
        this_month: typing.Callable[[], T_Result],
        today: typing.Callable[[], T_Result],
        yesterday: typing.Callable[[], T_Result],
        this_year: typing.Callable[[], T_Result],
        last_year: typing.Callable[[], T_Result],
        this_quarter: typing.Callable[[], T_Result],
        last_quarter: typing.Callable[[], T_Result],
        last3months: typing.Callable[[], T_Result],
        last6months: typing.Callable[[], T_Result],
        last12months: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchUsingBasicRequestTimeRangeType.CUSTOM:
            return custom()
        if self is SearchUsingBasicRequestTimeRangeType.LAST7DAYS:
            return last7days()
        if self is SearchUsingBasicRequestTimeRangeType.LAST30DAYS:
            return last30days()
        if self is SearchUsingBasicRequestTimeRangeType.LAST_MONTH:
            return last_month()
        if self is SearchUsingBasicRequestTimeRangeType.THIS_MONTH:
            return this_month()
        if self is SearchUsingBasicRequestTimeRangeType.TODAY:
            return today()
        if self is SearchUsingBasicRequestTimeRangeType.YESTERDAY:
            return yesterday()
        if self is SearchUsingBasicRequestTimeRangeType.THIS_YEAR:
            return this_year()
        if self is SearchUsingBasicRequestTimeRangeType.LAST_YEAR:
            return last_year()
        if self is SearchUsingBasicRequestTimeRangeType.THIS_QUARTER:
            return this_quarter()
        if self is SearchUsingBasicRequestTimeRangeType.LAST_QUARTER:
            return last_quarter()
        if self is SearchUsingBasicRequestTimeRangeType.LAST3MONTHS:
            return last3months()
        if self is SearchUsingBasicRequestTimeRangeType.LAST6MONTHS:
            return last6months()
        if self is SearchUsingBasicRequestTimeRangeType.LAST12MONTHS:
            return last12months()
