

import typing

StackSetOperationResultStatus = typing.Union[
    typing.Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"], typing.Any
]
