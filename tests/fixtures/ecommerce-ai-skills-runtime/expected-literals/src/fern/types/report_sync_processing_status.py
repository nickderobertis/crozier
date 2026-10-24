

import typing

ReportSyncProcessingStatus = typing.Union[
    typing.Literal["IN_QUEUE", "IN_PROGRESS", "DONE", "CANCELLED", "FATAL"], typing.Any
]
