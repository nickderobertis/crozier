

import typing

TestExecutionStatus = typing.Union[
    typing.Literal["NOT_STARTED", "IN_PROGRESS", "PASSED", "FAILED", "NOT_TESTED", "ENDED_PREMATURELY"], typing.Any
]
