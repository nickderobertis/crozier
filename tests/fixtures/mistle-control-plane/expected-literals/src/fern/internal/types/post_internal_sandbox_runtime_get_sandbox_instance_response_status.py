

import typing

PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus = typing.Union[
    typing.Literal[
        "pending",
        "starting",
        "started",
        "initializing",
        "running",
        "degraded",
        "reconnecting",
        "stopping",
        "stopped",
        "failed",
    ],
    typing.Any,
]
