

import typing

TaskState = typing.Union[
    typing.Literal[
        "success",
        "running",
        "failed",
        "upstream_failed",
        "skipped",
        "up_for_retry",
        "up_for_reschedule",
        "queued",
        "none",
        "scheduled",
        "deferred",
        "removed",
        "restarting",
    ],
    typing.Any,
]
