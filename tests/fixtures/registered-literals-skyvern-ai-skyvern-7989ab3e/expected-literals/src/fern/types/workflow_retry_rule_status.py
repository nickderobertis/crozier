

import typing

WorkflowRetryRuleStatus = typing.Union[
    typing.Literal["completed", "failed", "terminated", "canceled", "timed_out"], typing.Any
]
