

import typing

StackSetOperationStatus = typing.Union[
    typing.Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED", "QUEUED"], typing.Any
]
