

import typing

WorkflowRunStatus = typing.Union[
    typing.Literal[
        "created", "queued", "running", "failed", "terminated", "canceled", "timed_out", "completed", "paused"
    ],
    typing.Any,
]
