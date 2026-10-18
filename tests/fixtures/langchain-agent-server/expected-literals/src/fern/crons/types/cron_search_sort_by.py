

import typing

CronSearchSortBy = typing.Union[
    typing.Literal["cron_id", "assistant_id", "thread_id", "next_run_date", "end_time", "created_at", "updated_at"],
    typing.Any,
]
