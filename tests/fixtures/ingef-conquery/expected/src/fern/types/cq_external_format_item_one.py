

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CqExternalFormatItemOne(enum.StrEnum):
    """
    EXTRA columns supply auxiliary data to be emitted as columns named after each columns header. Otherwise describes schemes to do date aggregation on one or multiple columns: - EVENT_DATE selects a single column as the source of the selected date - START_DATE selects a column as the start of a DateRange - END_DATE selects a column as the end of a DateRange - DATE_RANGE selects a column as a full DateRange - DATE_SET selects a column as containing a date-set - ALL placeholder, to aggregate infinite/all dateset
    Combining multiple of the date aggregations is possible but except for START_DATE/END_DATE will create bogus results.
    """

    EXTRA = "EXTRA"
    EVENT_DATE = "EVENT_DATE"
    START_DATE = "START_DATE"
    END_DATE = "END_DATE"
    DATE_RANGE = "DATE_RANGE"
    DATE_SET = "DATE_SET"
    ALL = "ALL"

    def visit(
        self,
        extra: typing.Callable[[], T_Result],
        event_date: typing.Callable[[], T_Result],
        start_date: typing.Callable[[], T_Result],
        end_date: typing.Callable[[], T_Result],
        date_range: typing.Callable[[], T_Result],
        date_set: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CqExternalFormatItemOne.EXTRA:
            return extra()
        if self is CqExternalFormatItemOne.EVENT_DATE:
            return event_date()
        if self is CqExternalFormatItemOne.START_DATE:
            return start_date()
        if self is CqExternalFormatItemOne.END_DATE:
            return end_date()
        if self is CqExternalFormatItemOne.DATE_RANGE:
            return date_range()
        if self is CqExternalFormatItemOne.DATE_SET:
            return date_set()
        if self is CqExternalFormatItemOne.ALL:
            return all_()
