

import typing

RunStatus = typing.Union[
    typing.Literal[
        "created", "queued", "running", "paused", "timed_out", "failed", "terminated", "completed", "canceled"
    ],
    typing.Any,
]
