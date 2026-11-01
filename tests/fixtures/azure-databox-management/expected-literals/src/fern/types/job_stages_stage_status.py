

import typing

JobStagesStageStatus = typing.Union[
    typing.Literal["None", "InProgress", "Succeeded", "Failed", "Cancelled", "Cancelling", "SucceededWithErrors"],
    typing.Any,
]
