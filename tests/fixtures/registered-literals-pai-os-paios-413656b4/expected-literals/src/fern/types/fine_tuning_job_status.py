

import typing

FineTuningJobStatus = typing.Union[
    typing.Literal["validating_files", "queued", "running", "succeeded", "failed", "cancelled"], typing.Any
]
