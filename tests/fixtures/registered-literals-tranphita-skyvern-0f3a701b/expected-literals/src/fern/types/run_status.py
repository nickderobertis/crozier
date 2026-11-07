

import typing

RunStatus = typing.Union[
    typing.Literal["created", "queued", "running", "timed_out", "failed", "terminated", "completed", "canceled"],
    typing.Any,
]
