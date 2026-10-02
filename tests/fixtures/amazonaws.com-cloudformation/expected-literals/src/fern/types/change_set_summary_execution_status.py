

import typing

ChangeSetSummaryExecutionStatus = typing.Union[
    typing.Literal["UNAVAILABLE", "AVAILABLE", "EXECUTE_IN_PROGRESS", "EXECUTE_COMPLETE", "EXECUTE_FAILED", "OBSOLETE"],
    typing.Any,
]
