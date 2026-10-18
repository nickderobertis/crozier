

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CronSearchSortBy(enum.StrEnum):
    """
    The field to sort by.
    """

    CRON_ID = "cron_id"
    ASSISTANT_ID = "assistant_id"
    THREAD_ID = "thread_id"
    NEXT_RUN_DATE = "next_run_date"
    END_TIME = "end_time"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"

    def visit(
        self,
        cron_id: typing.Callable[[], T_Result],
        assistant_id: typing.Callable[[], T_Result],
        thread_id: typing.Callable[[], T_Result],
        next_run_date: typing.Callable[[], T_Result],
        end_time: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CronSearchSortBy.CRON_ID:
            return cron_id()
        if self is CronSearchSortBy.ASSISTANT_ID:
            return assistant_id()
        if self is CronSearchSortBy.THREAD_ID:
            return thread_id()
        if self is CronSearchSortBy.NEXT_RUN_DATE:
            return next_run_date()
        if self is CronSearchSortBy.END_TIME:
            return end_time()
        if self is CronSearchSortBy.CREATED_AT:
            return created_at()
        if self is CronSearchSortBy.UPDATED_AT:
            return updated_at()
