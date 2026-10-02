

import typing

BuildSystemSharedDtoJobRunStatus = typing.Union[
    typing.Literal["Ready", "InProgress", "Succeeded", "Cancelled", "Failed"], typing.Any
]
