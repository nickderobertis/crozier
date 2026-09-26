

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTimeEntriesRequestSortField(enum.StrEnum):
    TIME_ENTRY_DATE = "timeEntryDate"
    JOB_NO = "jobNo"
    USER = "user"

    def visit(
        self,
        time_entry_date: typing.Callable[[], T_Result],
        job_no: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTimeEntriesRequestSortField.TIME_ENTRY_DATE:
            return time_entry_date()
        if self is GetTimeEntriesRequestSortField.JOB_NO:
            return job_no()
        if self is GetTimeEntriesRequestSortField.USER:
            return user()
