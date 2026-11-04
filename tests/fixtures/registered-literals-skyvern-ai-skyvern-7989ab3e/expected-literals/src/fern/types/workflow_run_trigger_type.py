

import typing

WorkflowRunTriggerType = typing.Union[
    typing.Literal["manual", "mcp", "api", "scheduled", "webhook", "job_recipe_extract", "job_recipe_apply"], typing.Any
]
