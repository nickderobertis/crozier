

import typing

PilotRuntimeStatusStopReason = typing.Union[
    typing.Literal["graceful_shutdown", "startup_failure", "worker_shutdown_timeout"], typing.Any
]
