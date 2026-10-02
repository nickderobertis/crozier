

import typing

AsyncJobStatus = typing.Union[
    typing.Literal["COMPLETED", "FAILED", "IN_PROGRESS", "READY_TO_DOWNLOAD", "SUBMITTED"], typing.Any
]
