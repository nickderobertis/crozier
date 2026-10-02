

import typing

StackInstanceDetailedStatus = typing.Union[
    typing.Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED", "INOPERABLE"], typing.Any
]
