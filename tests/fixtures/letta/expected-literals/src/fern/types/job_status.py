

import typing

JobStatus = typing.Union[
    typing.Literal["created", "running", "completed", "failed", "pending", "cancelled", "expired"], typing.Any
]
