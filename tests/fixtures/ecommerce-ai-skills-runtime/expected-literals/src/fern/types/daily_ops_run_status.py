

import typing

DailyOpsRunStatus = typing.Union[
    typing.Literal["scheduled", "running", "completed", "empty", "failed", "blocked"], typing.Any
]
