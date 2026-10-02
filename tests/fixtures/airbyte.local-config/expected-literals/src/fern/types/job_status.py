

import typing

JobStatus = typing.Union[
    typing.Literal["pending", "running", "incomplete", "failed", "succeeded", "cancelled"], typing.Any
]
