

import typing

WorkflowGetByIdResponseStatus = typing.Union[
    typing.Literal[
        "success", "running", "not_run", "failed", "error", "failing", "on_hold", "canceled", "unauthorized"
    ],
    typing.Any,
]
