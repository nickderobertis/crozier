

import typing

ProposalExecutionStatus = typing.Union[
    typing.Literal["pending", "executing", "executed", "failed", "blocked"], typing.Any
]
