

import typing

RunningState = typing.Union[
    typing.Literal[
        "UNKNOWN",
        "NOT_STARTED",
        "PUBLISHED",
        "PENDING",
        "WAITING_FOR_CLUSTER",
        "WAITING_FOR_RESOURCES",
        "STARTED",
        "SUCCESS",
        "FAILED",
        "ABORTED",
    ],
    typing.Any,
]
