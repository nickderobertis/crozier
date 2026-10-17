

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CronSearchSelectItem(enum.StrEnum):
    CRON_ID = "cron_id"
    ASSISTANT_ID = "assistant_id"
    THREAD_ID = "thread_id"
    ON_RUN_COMPLETED = "on_run_completed"
    END_TIME = "end_time"
    SCHEDULE = "schedule"
    TIMEZONE = "timezone"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    USER_ID = "user_id"
    PAYLOAD = "payload"
    NEXT_RUN_DATE = "next_run_date"
    METADATA = "metadata"
    ENABLED = "enabled"

    def visit(
        self,
        cron_id: typing.Callable[[], T_Result],
        assistant_id: typing.Callable[[], T_Result],
        thread_id: typing.Callable[[], T_Result],
        on_run_completed: typing.Callable[[], T_Result],
        end_time: typing.Callable[[], T_Result],
        schedule: typing.Callable[[], T_Result],
        timezone: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        user_id: typing.Callable[[], T_Result],
        payload: typing.Callable[[], T_Result],
        next_run_date: typing.Callable[[], T_Result],
        metadata: typing.Callable[[], T_Result],
        enabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CronSearchSelectItem.CRON_ID:
            return cron_id()
        if self is CronSearchSelectItem.ASSISTANT_ID:
            return assistant_id()
        if self is CronSearchSelectItem.THREAD_ID:
            return thread_id()
        if self is CronSearchSelectItem.ON_RUN_COMPLETED:
            return on_run_completed()
        if self is CronSearchSelectItem.END_TIME:
            return end_time()
        if self is CronSearchSelectItem.SCHEDULE:
            return schedule()
        if self is CronSearchSelectItem.TIMEZONE:
            return timezone()
        if self is CronSearchSelectItem.CREATED_AT:
            return created_at()
        if self is CronSearchSelectItem.UPDATED_AT:
            return updated_at()
        if self is CronSearchSelectItem.USER_ID:
            return user_id()
        if self is CronSearchSelectItem.PAYLOAD:
            return payload()
        if self is CronSearchSelectItem.NEXT_RUN_DATE:
            return next_run_date()
        if self is CronSearchSelectItem.METADATA:
            return metadata()
        if self is CronSearchSelectItem.ENABLED:
            return enabled()
