

import typing

CronSearchSelectItem = typing.Union[
    typing.Literal[
        "cron_id",
        "assistant_id",
        "thread_id",
        "on_run_completed",
        "end_time",
        "schedule",
        "timezone",
        "created_at",
        "updated_at",
        "user_id",
        "payload",
        "next_run_date",
        "metadata",
        "enabled",
    ],
    typing.Any,
]
