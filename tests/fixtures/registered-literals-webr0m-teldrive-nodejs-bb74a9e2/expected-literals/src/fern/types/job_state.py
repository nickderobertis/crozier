

import typing

JobState = typing.Union[
    typing.Literal["available", "cancelled", "completed", "discarded", "pending", "retryable", "running", "scheduled"],
    typing.Any,
]
